#!/usr/bin/env python3
"""
FIFOCache System model
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache
    """

    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Assign a key-value pair to the cache if the limit is not reached.
        Otherwise, delete the first item and add the new key-value pair.
        """
        if key is not None and item is not None:
            if len(self.keys) >= self.MAX_ITEMS:
                if key not in self.keys:
                    del_key = self.keys.pop(0)
                    del self.cache_data[del_key]
            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get the value associated with the given key from the cache.
        If the key does not exist, return None.
        """
        return self.cache_data.get(key, None)
