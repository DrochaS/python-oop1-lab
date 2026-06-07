#!/usr/bin/env python3

class Book:
    """
    A class to represent a book.
    """

    def __init__(self, title, page_count):
        """
        Initialize the Book with a title and page count.
        """
        self.title = title
        self._page_count = 0  # Initialize with a default value
        self.page_count = page_count

    @property
    def page_count(self):
        """
        Get the page count.
        """
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """
        Set the page count, ensuring it's an integer.
        """
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        """
        Simulate turning a page.
        """
        print("Flipping the page...wow, you read fast!")
