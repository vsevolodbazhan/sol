from node import Node


class List:
    def __init__(self):
        """
        Create a new doubly linked list.
        """
        self.head = None
        self.tail = None

    def __iter__(self):
        """
        Traverse the list in forward direction.
        """
        pass

    def __reversed__(self):
        """
        Traverse the list in reverse direction.
        """
        pass

    def append(self, data):
        """
        Insert an element to the end of the list.
        """
        pass

    def prepend(self, data):
        """
        Insert an element to the beginning of the list.
        """
        pass

    def insert_before(self, existing_node, new_node):
        """
        Insert a node before a given node.
        """
        pass

    def insert_after(self, existing_node, new_node):
        """
        Insert a node after a given one.
        """
        pass

    def remove(self, node):
        """
        Remove a given node from the list.
        """
        pass

    def find(self, data):
        """
        Get the first node that contains a given data.
        Return `None` if no such node is present in the list.
        """
        pass
