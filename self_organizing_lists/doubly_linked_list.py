from node import Node


class List:
    def __init__(self):
        """
        Create a new doubly linked list.
        """
        self.head = None
        self.tail = None

    def __repr__(self):
        """
        Return an unambiguous representation of an object.
        """
        return (f'{self.__class__.__name__}('
                f'head={self.head!r}, tail={self.tail!r})')

    def __str__(self):
        """
        Return elements of the list as a string.
        """
        return f'{[element for element in self]}'

    def __iter__(self):
        """
        Traverse the list in forward direction.
        """
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __reversed__(self):
        """
        Traverse the list in reverse direction.
        """
        node = self.tail
        while node:
            yield node.data
            node = node.prev

    def append(self, data):
        """
        Insert an element to the end of the list.
        """
        new_node = Node(data)
        if self.tail:
            self.insert_after(self.tail, new_node)
        else:
            self.head = new_node
            self.tail = new_node

    def prepend(self, data):
        """
        Insert an element to the beginning of the list.
        """
        new_node = Node(data)
        if self:
            self.insert_before(self.head, new_node)
        else:
            self.head = new_node
            self.tail = new_node

    def insert_before(self, existing_node, new_node):
        """
        Insert a node before a given node.
        """
        new_node.next = existing_node
        if existing_node is self.head:
            new_node.prev = None
            self.head = new_node
        else:
            new_node.prev = existing_node.prev
            existing_node.prev.next = new_node
        existing_node.prev = new_node

    def insert_after(self, existing_node, new_node):
        """
        Insert a node after a given one.
        """
        new_node.prev = existing_node
        if existing_node is self.tail:
            new_node.next = None
            self.tail = new_node
        else:
            new_node.next = existing_node.next
            existing_node.next.prev = new_node
        existing_node.next = new_node

    def remove(self, node):
        """
        Remove a given node from the list.
        """
        # A node might be the head of the list.
        if node is self.head:
            self.head = node.next
        else:
            node.prev.next = node.next
        # Or a node might be the tail of the list.
        if node is self.tail:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

    def find(self, data):
        """
        Get the first node that contains a given data.
        Return `None` if no such node is present in the list.
        """
        node = self.head
        while node:
            if node.data == data:
                self.rearrange(node)
                return node
            node = node.next
        return None

    def rearrange(self, node):
        return
