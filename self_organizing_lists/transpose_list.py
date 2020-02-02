from doubly_linked_list import List


class TransposeList(List):
    def rearrange(self, node):
        """
        Apply transpose method.
        """
        if node is not self.head:
            prev = node.prev
            self.remove(node)
            self.insert_before(prev, node)
