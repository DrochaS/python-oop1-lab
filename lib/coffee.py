#!/usr/bin/env python3

class Coffee:
    """
    A class to represent a coffee.
    """

    def __init__(self, size, price):
        """
        Initialize the Coffee with a size and price.
        """
        self._size = None  # Initialize with a default value
        self.size = size
        self.price = price

    @property
    def size(self):
        """
        Get the coffee size.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Set the coffee size, ensuring it's Small, Medium, or Large.
        """
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        """
        Leave a tip for the coffee, increasing its price.
        """
        print("This coffee is great, here’s a tip!")
        self.price += 1
