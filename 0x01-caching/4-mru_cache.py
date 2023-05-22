#!/usr/bin/env python3
"""
LRUCache System model
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache
    """

    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()
        self.used_key = []

    def put(self, key, item):
        """
        Assign a key-value pair to the cache if the limit is not reached.
        Otherwise, delete the least recently used item and update the used key.
        """
        if key is not None and item is not None:
            if len(self.used_key) >= self.MAX_ITEMS:
                if key not in self.used_key:
                    del_key = self.used_key.pop()
                    del self.cache_data[del_key]
            self.used_key = [key] + [k for k in self.used_key if k != key]
            self.cache_data[key] = item

    def get(self, key):
        """
        Get the value associated with the given key from the cache.
        If the key does not exist, return None.
        Update the used key to reflect the most recently used item.
        """
        if key not in self.used_key:
            return None
        self.used_key = [key] + [k for k in self.used_key if k != key]
        return self.cache_data.get(key, None)
