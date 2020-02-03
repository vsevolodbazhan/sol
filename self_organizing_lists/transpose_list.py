from .doubly_linked_list import List


class TransposeList(List):
    """
    Doubly linked list that implements transpose method.
    """

    def _rearrange(self, node):
        """
        Apply transpose method.
        """
        if node is not self.head:
            prev = node.prev
            self._remove(node)
            self._insert_before(prev, node)
