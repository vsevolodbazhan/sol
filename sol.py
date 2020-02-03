__all__ = ['List', 'MoveToFrontList', 'TransposeList']


class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        """
        Return an unambiguous representation of an object.
        """
        next = self.next.data if self.next else None
        prev = self.prev.data if self.prev else None
        return (f'{self.__class__.__name__}('
                f'{self.data!r}, next={next!r}, prev={prev!r})')

    def __str__(self):
        """
        Return value as a string.
        """
        return f'{self.data}'


class NotEmptyError(ValueError):
    """
    Raised when a list not is empty.
    """


class List:
    """
    Doubly linked list.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    @classmethod
    def from_iterable(cls, iterable):
        """
        Alternate constructor for `List`.
        Gets data from a single `iterable` argument.

        >>> a = List.from_iterable([1, 2, 3])
        >>> print(a)
        [1, 2, 3]
        >>> b = List.from_iterable(('Hello', 'World'))
        >>> print(b)
        ['Hello', 'World']
        """
        new_list = cls()
        new_list.extend(iterable)
        return new_list

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

    def __len__(self):
        return self.size

    def append(self, data):
        """
        Insert an element to the end of the list.

        >>> a = List()
        >>> a.append(1)
        >>> a.append(2)
        >>> print(a)
        [1, 2]
        """
        new_node = Node(data)
        if self.tail:
            self._insert_after(self.tail, new_node)
        else:
            self._insert_first(new_node)

    def prepend(self, data):
        """
        Insert an element to the beginning of the list.

        >>> a = List()
        >>> a.prepend(1)
        >>> a.prepend(0)
        >>> print(a)
        [0, 1]
        """
        new_node = Node(data)
        if self.head:
            self._insert_before(self.head, new_node)
        else:
            self._insert_first(new_node)

    def _insert_first(self, new_node):
        """
        Insert a node into the empty list.
        Raise `NotEmptyError` if the list is not empty.
        """
        if self.size > 0:
            raise NotEmptyError('List must be empty')
        self.head = new_node
        self.tail = new_node
        self.size += 1

    def _insert_before(self, existing_node, new_node):
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
        self.size += 1

    def _insert_after(self, existing_node, new_node):
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
        self.size += 1

    def extend(self, iterable):
        """
        Insert items from `iterable` to the end of the list.

        >>> a = List()
        >>> b = [1, 2, 3]
        >>> a.extend(b)
        >>> print(a)
        [1, 2, 3]
        """
        for item in iterable:
            self.append(item)

    def pop_back(self):
        """
        Remove the last element of the list.

        >>> a = List.from_iterable([1, 2, 3])
        >>> print(a)
        [1, 2, 3]
        >>> a.pop_back()
        >>> print(a)
        [1, 2]
        """
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1

    def pop_front(self):
        """
        Remove the first element of the list.

        >>> a = List.from_iterable([1, 2, 3])
        >>> print(a)
        [1, 2, 3]
        >>> a.pop_front()
        >>> print(a)
        [2, 3]
        """
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1

    def erase(self, data):
        """
        Erase all elements of the list that
        contain a given data.

        >>> a = List.from_iterable([1, 2, 3, 3, 3, 4])
        >>> print(a)
        [1, 2, 3, 3, 3, 4]
        >>> a.erase(3)
        >>> print(a)
        [1, 2, 4]
        """
        for node in self._nodes():
            next = node.next
            if node.data == data:
                self._remove(node)
            node = next

    def _remove(self, node):
        """
        Remove a given node from the list.
        """
        if node is self.head:
            self.pop_front()
        elif node is self.tail:
            self.pop_back()
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.size -= 1

    def find(self, data):
        """
        Get the first node that contains a given data.
        Return `None` if no such node is present in the list.
        """
        node = self.head
        while node:
            if node.data == data:
                self._rearrange(node)
                return node
            node = node.next
        return None

    def _rearrange(self, node):
        """
        Apply self-organizing method.
        """
        return

    def _nodes(self):
        """
        Traverse the list _nodes in forward direction.
        """
        node = self.head
        while node:
            yield node
            node = node.next


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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
