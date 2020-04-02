class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def __repr__(self):
        """
        Return an unambiguous representation of an object.
        """
        next_node = self.next_node.data if self.next_node else None
        prev_node = self.prev_node.data if self.prev_node else None
        return (f'{self.__class__.__name__}('
                f'{self.data!r}, next_node={next_node!r}, prev_node={prev_node!r})')

    def __str__(self):
        """
        Return value as a string.
        """
        return f'{self.data}'
