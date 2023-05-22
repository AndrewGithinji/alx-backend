#!/usr/bin/env python3
"""
MRUCache   System model
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache
    """

    def __init__(self):
        """
        Initialize Cache
        """
        super().__init__()
        self.used_key = []

    def put(self, key, item):
        """
        assign a key to value to cache if limit not reached
        otherwise delete most  used item and update used key
        """
        if key and item:
            if len(self.used_key) >= self.MAX_ITEMS:
                if key not in self.used_key:
                    print(f"DISCARD: {self.used_key[0]}")
                    del self.cache_data[self.used_key[0]]
                del self.used_key[0]
            self.used_key = [key] + self.used_key
            self.cache_data[key] = item

    def get(self, key):
        """
            get item from cache if it exists other none
            update used key
        """
        if key not in self.used_key:
            return None
        del self.used_key[self.used_key.index(key)]
        self.used_key = [key] + self.used_key
        return self.cache_data[key]
