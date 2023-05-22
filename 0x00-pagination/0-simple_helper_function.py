#!/usr/bin/env python3
"""
Util Function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    return a tuple of size two containing a start index and an end index
    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    return ((page - 1) * page_size, page * page_size)
