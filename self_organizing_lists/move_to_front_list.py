from .doubly_linked_list import List


class MoveToFrontList(List):
    """
    Doubly linked list that implements move to front method.
    """

    def _rearrange(self, node):
        """
        Apply move to front method.
        """
        if node is not self.head:
            self._remove(node)
            self._insert_before(self.head, node)
