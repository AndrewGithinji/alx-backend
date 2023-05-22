#!/usr/bin/env python3
"""
Simple Pagination
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
         return the appropriate page of the dataset
        """
        self.__dataset = self.dataset()
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        index = self.index_range(page, page_size)
        res = self.__dataset[index[0]:index[1]] if index[0] < len(
            self.__dataset) and index[1] < len(self.__dataset) else []
        return res

    def index_range(self, page: int, page_size: int) -> tuple:
        """
        return a tuple of size two containing a start index and an end index
        Page numbers are 1-indexed, i.e. the first page is page 1.
        """
        return ((page - 1) * page_size, page * page_size)
