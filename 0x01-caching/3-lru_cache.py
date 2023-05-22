#!/usr/bin/env python3
"""
LRUCache  System model
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache
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
        otherwise delete least used item and update used key
        """
        if key and item:
            if len(self.used_key) >= self.MAX_ITEMS:
                if key not in self.used_key:
                    print(f"DISCARD: {self.used_key[-1]}")
                    del self.cache_data[self.used_key[-1]]
                del self.used_key[-1]
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
