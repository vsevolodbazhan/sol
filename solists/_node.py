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
