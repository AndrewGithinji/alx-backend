#!/usr/bin/env python3
"""
LIFOCache  System model
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache
    """

    def __init__(self):
        """
        Initialize  the cache
            keys: list of key in order
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        assign a key to value to cache if limit not reached
        otherwise delete the last item
        """
        if key and item:
            if len(self.keys) >= self.MAX_ITEMS:
                if key not in self.keys:
                    print(f"DISCARD: {self.keys[-1]}")
                    del self.cache_data[self.keys[-1]]
                del self.keys[-1]
            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        get item from cache if it exists other none
        """
        if key not in self.keys:
            return None
        return self.cache_data[key]
