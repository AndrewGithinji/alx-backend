#!/usr/bin/env python3
""" 0-basic_cache.py
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Cache System that has no limit
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        Set item to cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get item from cache if it exists, otherwise return None
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
