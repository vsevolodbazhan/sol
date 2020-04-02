from .doubly_linked_list import List

__all__ = ['TransposeList']


class TransposeList(List):
    """
    Doubly linked list that implements transpose method.

    >>> a = TransposeList.from_iterable([1, 2, 3])
    >>> print(a)
    [1, 2, 3]
    >>> 3 in a
    True
    >>> print(a)
    [1, 3, 2]
    >>> 2 in a
    True
    >>> print(a)
    [1, 2, 3]
    >>> 5 in a
    False
    >>> print(a)
    [1, 2, 3]
    """

    def _rearrange(self, node):
        """
        Apply transpose method.
        """
        if node is not self.head:
            prev_node = node.prev_node
            self._remove(node)
            self._insert_before(prev_node, node)
