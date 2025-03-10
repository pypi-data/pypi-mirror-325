"""
Copyright Harrison Erd

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
contributors may be used to endorse or promote products derived from
this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import asyncio
import os

import aiofiles
import orjson


class PickleDB:
    """
    A barebones orjson-based key-value store with essential methods:
    set, get, save, remove, purge, and all.
    """

    def __init__(self, location):
        """
        Initialize the PickleDB object.

        Args:
            location (str): Path to the JSON file.
        """
        self.location = os.path.expanduser(location)
        self._load()

    def __setitem__(self, key, value):
        """
        Wraps the `set` method to allow `db[key] = value`. See `set`
        method for details.
        """
        return self.set(key, value)

    def __getitem__(self, key):
        """
        Wraps the `get` method to allow `value = db[key]`. See `get`
        method for details.
        """
        return self.get(key)

    def _load(self):
        """
        Load data from the JSON file if it exists, or initialize an empty
        database.
        """
        if (os.path.exists(self.location) and
                os.path.getsize(self.location) > 0):
            try:
                with open(self.location, "rb") as f:
                    self.db = orjson.loads(f.read())
            except Exception as e:
                raise RuntimeError(f"{e}\nFailed to load database.")
        else:
            self.db = {}

    def save(self, option=0):
        """
        Save the database to the file using an atomic save.

        Args:
            options (int): `orjson.OPT_*` flags to configure
                           serialization behavior.

        Behavior:
            - Writes to a temporary file and replaces the
              original file only after the write is successful,
              ensuring data integrity.

        Returns:
            bool: True if save was successful, False if not.
        """
        temp_location = f"{self.location}.tmp"
        try:
            with open(temp_location, "wb") as temp_file:
                temp_file.write(orjson.dumps(self.db, option=option))
            os.replace(temp_location, self.location)
            return True
        except Exception as e:
            print(f"Failed to save database: {e}")
            return False

    def set(self, key, value):
        """
        Add or update a key-value pair in the database.

        Args:
            key (any): The key to set. If the key is not a string, it
                       will be converted to a string.
            value (any): The value to associate with the key.

        Behavior:
            - If the key already exists, its value will be updated.
            - If the key does not exist, it will be added to the
              database.

        Returns:
            bool: True if the operation succeeds.
        """
        key = str(key) if not isinstance(key, str) else key
        self.db[key] = value
        return True

    def remove(self, key):
        """
        Remove a key and its value from the database.

        Args:
            key (any): The key to delete. If the key is not a string,
                       it will be converted to a string.

        Returns:
            bool: True if the key was deleted, False if the key does
                  not exist.
        """
        key = str(key) if not isinstance(key, str) else key
        if key in self.db:
            del self.db[key]
            return True
        return False

    def purge(self):
        """
        Clear all keys from the database.

        Returns:
            bool: True if the operation succeeds.
        """
        self.db.clear()
        return True

    def get(self, key):
        """
        Get the value associated with a key.

        Args:
            key (any): The key to retrieve. If the key is not a
                       string, it will be converted to a string.

        Returns:
            any: The value associated with the key, or None if the
            key does not exist.
        """
        key = str(key) if not isinstance(key, str) else key
        return self.db.get(key)

    def all(self):
        """
        Get a list of all keys in the database.

        Returns:
            list: A list of all keys.
        """
        return list(self.db.keys())


class AsyncPickleDB:
    """
    Provides an async version of pickleDB
    """

    def __init__(self, location, batch_size=1, cleanup_interval=5):
        """
        Initialize the PickleDB object.

        Args:
            location (str): Path to the JSON file.
            batch_size (int): Number of operations to batch together.
            cleanup_interval (int): Number of operations between cleanups.
        """
        self.location = os.path.expanduser(location)
        self._lock = asyncio.Lock()
        self.batch_size = batch_size
        self.cleanup_interval = cleanup_interval
        self._batch = []
        self._operation_count = 0
        self._cache = {}

    async def __setitem__(self, key, value):
        """
        Allow the syntax db[key] = value.
        """
        return await self.set(key, value)

    async def __getitem__(self, key):
        """
        Allow the syntax value = db[key].
        """
        return await self.get(key)

    async def _save_batch(self):
        """
        Save a batch of entries to the file using JSON Lines format,
        then trigger file compaction to remove stale entries.

        Returns:
            bool: True if save was successful, False otherwise.
        """
        try:
            async with self._lock:
                async with aiofiles.open(self.location, "ab") as f:
                    data = b''.join([orjson.dumps(entry) + b'\n' for entry in self._batch])
                    await f.write(data)
                self._batch.clear()
                self._operation_count += len(self._batch)
            # Perform cleanup periodically
            if self._operation_count >= self.cleanup_interval:
                await self._cleanup_removed_keys()
                self._operation_count = 0
            return True
        except Exception as e:
            print(f"Failed to save batch: {e}")
            return False

    async def _cleanup_removed_keys(self):
        """
        Compact the file by reading all the operations (sets and removals),
        applying them to derive the current state of the database,
        and rewriting the file with only the latest state.
        """
        async with self._lock:
            if not os.path.exists(self.location):
                return
            try:
                state = {}
                async with aiofiles.open(self.location, "rb") as infile:
                    async for line in infile:
                        try:
                            entry = orjson.loads(line)
                        except Exception as e:
                            print(f"Error reading a line in cleanup: {e}")
                            continue
                        if "__remove__" in entry:
                            rm_key = entry["__remove__"]
                            if rm_key in state:
                                del state[rm_key]
                        else:
                            state.update(entry)
                async with aiofiles.open(self.location, "wb") as outfile:
                    for key, value in state.items():
                        await outfile.write(orjson.dumps({key: value}) + b'\n')
                self._cache = state  # Update in-memory cache
            except Exception as e:
                print(f"Failed to cleanup removed keys: {e}")

    async def set(self, key, value):
        """
        Set or update the value of a key.

        Args:
            key (any): The key to set (converted to string if needed).
            value (any): The value to associate.

        Returns:
            bool: True if successful.
        """
        if not isinstance(key, str):
            key = str(key)
        self._batch.append({key: value})
        self._cache[key] = value  # Update in-memory cache
        if len(self._batch) >= self.batch_size:
            return await self._save_batch()
        return True

    async def remove(self, key):
        """
        Mark a key for removal.

        Args:
            key (any): The key to remove (converted to string if needed).

        Returns:
            bool: True if the removal operation succeeds.
        """
        if not isinstance(key, str):
            key = str(key)
        self._batch.append({"__remove__": key})
        if key in self._cache:
            del self._cache[key]  # Update in-memory cache
        if len(self._batch) >= self.batch_size:
            return await self._save_batch()
        return True

    async def purge(self):
        """
        Clear the entire database by emptying the file.

        Returns:
            bool: True if purge is successful.
        """
        async with self._lock:
            try:
                async with aiofiles.open(self.location, "w") as f:
                    await f.write("")
                self._batch.clear()
                self._cache.clear()
                return True
            except Exception as e:
                print(f"Failed to purge database: {e}")
                return False

    async def get(self, key):
        """
        Retrieve the value associated with a given key.

        Args:
            key (any): The key to search for (converted to string if needed).

        Returns:
            any: The value if the key exists, or None otherwise.
        """
        if not isinstance(key, str):
            key = str(key)
        # Check in-memory cache first
        if key in self._cache:
            return self._cache[key]
        async with self._lock:
            if os.path.exists(self.location) and os.path.getsize(self.location) > 0:
                try:
                    async with aiofiles.open(self.location, "rb") as f:
                        async for line in f:
                            entry = orjson.loads(line)
                            if key in entry:
                                return entry[key]
                except Exception as e:
                    print(f"Failed to get key: {e}")
            return None

    async def all(self):
        """
        Retrieve a list of all keys present in the database.

        Returns:
            list: A list of keys with duplicates removed.
        """
        async with self._lock:
            keys = set(self._cache.keys())
            if os.path.exists(self.location) and os.path.getsize(self.location) > 0:
                try:
                    async with aiofiles.open(self.location, "rb") as f:
                        async for line in f:
                            entry = orjson.loads(line)
                            keys.update(entry.keys())
                except Exception as e:
                    print(f"Failed to get all keys: {e}")
        return list(keys)

