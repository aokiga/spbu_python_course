"""Array class implementation for homework 2."""


class Array(object):  # noqa: WPS214
    """Array class implementation."""

    def __init__(self, *args):
        """
        Create Array from given objects.

        Args:
            args: Given objects to store.
        """
        self._array_data = tuple(args)

    def __len__(self):
        """
        Return length of Array.

        Returns:
            Length of Array.
        """
        return len(self._array_data)

    def __getitem__(self, index):
        """
        Get item from index.

        Args:
            index: Index of the Array.

        Returns:
            Item from index in the Array.
        """
        return self._array_data[index]

    def __eq__(self, other):
        """
        Check is the our Array is equal to other object.

        Args:
            other: Object to compare.

        Returns:
            True if our Array and other are equal, False otherwise.
        """
        if not isinstance(other, Array):
            return False
        return self._array_data == other.get_data()

    def __add__(self, other):
        """
        Concatenate our Array with other.

        Args:
            other: Array to concatenate with.

        Returns:
            Result of concatenation of our Array and other.

        Raises:
            TypeError: when other is not instance of Array.
        """
        if not isinstance(other, Array):
            raise TypeError
        new_data = self._array_data + other.get_data()
        return Array(*new_data)

    def __iter__(self):
        """
        Return iterator for Array.

        Returns:
            Iterator for Array.
        """
        return iter(self._array_data)

    def get_data(self):
        """
        Get data of the Array.

        Returns:
            Data of the Array.
        """
        return self._array_data

    def append(self, elem):
        """
        Add element to the end of the Array.

        Args:
            elem: Element to add.
        """
        self._array_data = self._array_data + (elem, )

    def index(self, elem):
        """
        Search for element in the Array, return it's first occurence index.

        Args:
            elem: Element to search.

        Returns:
            First occurence index if found, -1 otherwise.
        """
        if elem not in self._array_data:
            return -1
        return self._array_data.index(elem)

    def pop(self, index):
        """
        Remove element with given index and return it.

        Args:
            index: Index of element to remove.

        Returns:
            Removed element.
        """
        elem = self._array_data[index]
        before = self._array_data[:index]
        after = self._array_data[index + 1:]
        self._array_data = before + after
        return elem

    def remove(self, elem):
        """
        Remove first occurence of the element.

        Args:
            elem: Element to remove.

        Raises:
            ValueError: Raises ValueError if there is no such item.
        """
        index = self.index(elem)
        if index == -1:
            raise ValueError
        else:
            self.pop(index)
