import unittest
from solists import _node


class TestNode(unittest.TestCase):
    def test_init(self):
        n = _node.Node(0)
        self.assertEqual(n.data, 0)
        self.assertIsNone(n.next_node)
        self.assertIsNone(n.prev_node)

    def test_references(self):
        a = _node.Node(1)
        b = _node.Node(2)
        c = _node.Node(3, a, b)
        self.assertIs(c.next_node, a)
        self.assertIs(c.prev_node, b)

    def test_iterable_data(self):
        numbers = [1, 2, 3, 4, 5]
        n = _node.Node(numbers)
        self.assertEqual(n.data, numbers)
        self.assertIsNone(n.next_node)
        self.assertIsNone(n.prev_node)

    def test_custom_data(self):
        class Name:
            def __init__(self, name):
                self.name = name

            def __eq__(self, other):
                return self.name == other.name

        name = Name('Mike')
        n = _node.Node(name)
        self.assertEqual(n.data, Name('Mike'))
        self.assertIsNone(n.next_node)
        self.assertIsNone(n.prev_node)

    def test_repr_(self):
        a = _node.Node(1)
        b = _node.Node(2, a)
        self.assertEqual(
            b.__repr__(), f'Node({b.data}, next_node={a.data}, prev_node=None)')

    def test_str(self):
        n = _node.Node(1)
        self.assertEqual(n.__str__(), f'{n.data}')
