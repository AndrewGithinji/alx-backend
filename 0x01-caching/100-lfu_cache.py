#!/usr/bin/env python3
"""
LFUCache   System model
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache
    """

    def __init__(self):
        """
        Initialize Cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        assign a key to value to cache if limit not reached
        otherwise delete most  used item and update used key
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                a = self.cache_data.popitem(last=False)
                print("DISCARD: {}".format(a[0]))

    def get(self, key):
        """
            get item from cache if it exists other none
            update used key
        """
        if key not in self.cache_data.keys():
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
