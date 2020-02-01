class Node:
    def __init__(self, data, next=None, prev=None):
        """
        Create a new list node.
        """
        self.data = data
        self.next = next
        self.prev = prev
