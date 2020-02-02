from doubly_linked_list import List


class MoveToFrontList(List):
    def rearrange(self, node):
        """
        Apply move to front method.
        """
        if node is not self.head:
            self.remove(node)
            self.insert_before(self.head, node)
