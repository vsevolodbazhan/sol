from .doubly_linked_list import List

__all__ = ['MoveToFrontList']


class MoveToFrontList(List):
    """
    Doubly linked list that implements move to front method.

    >>> a = MoveToFrontList.from_iterable([1, 2, 3])
    >>> print(a)
    [1, 2, 3]
    >>> 3 in a
    True
    >>> print(a)
    [3, 1, 2]
    >>> 2 in a
    True
    >>> print(a)
    [2, 3, 1]
    >>> 5 in a
    False
    >>> print(a)
    [2, 3, 1]
    """

    def _rearrange(self, node):
        """
        Apply move to front method.
        """
        if node is not self.head:
            self._remove(node)
            self._insert_before(self.head, node)
