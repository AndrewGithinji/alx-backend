#!/usr/bin/env python3
"""
LFUCache System model
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache
    """

    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assign a key-value pair to the cache if the limit is not reached.
        Otherwise, delete the least frequently used item and update the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                del_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {del_key}")

    def get(self, key):
        """
        Get the value associated with the given key from the cache.
        If the key does not exist, return None.
        Update the cache to reflect the most recently used item.
        """
        if key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
