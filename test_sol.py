import unittest
import sol


class TestList(unittest.TestCase):
    def test_init(self):
        a = sol.List()
        self.assertIsNone(a.head)
        self.assertIsNone(a.tail)
        self.assertEqual(a.size, 0)

    def test_conversion(self):
        a = sol.List.from_iterable([1])
        self.assertEqual(a, [1])

        a = sol.List.from_iterable([])
        self.assertEqual(a, [])

        a = sol.List.from_iterable([1, 2, 3])
        self.assertEqual(a, [1, 2, 3])

    def test_append(self):
        a = sol.List()
        self.assertEqual(a, [])

        a.append(1)
        self.assertEqual(a, [1])

        a.append(2)
        a.append(3)
        self.assertEqual(a, [1, 2, 3])

    def test_prepend(self):
        a = sol.List()
        self.assertEqual(a, [])

        a.prepend(1)
        self.assertEqual(a, [1])

        a.prepend(2)
        a.prepend(3)
        self.assertEqual(a, [3, 2, 1])

    def test_extend(self):
        a = sol.List()
        self.assertEqual(a, [])

        a.extend([1, 2, 3])
        self.assertEqual(a, [1, 2, 3])

        a.extend([])
        self.assertEqual(a, [1, 2, 3])

        a.extend((4, 5, 6, 7))
        self.assertEqual(a, [1, 2, 3, 4, 5, 6, 7])

        a.extend([('A', 'B'), (2.5, 5.1)])
        self.assertEqual(
            a, [1, 2, 3, 4, 5, 6, 7, ('A', 'B'), (2.5, 5.1)])

    def test_pop_back(self):
        a = sol.List.from_iterable([1, 2, 3])
        self.assertEqual(a, [1, 2, 3])

        a.pop_back()
        self.assertEqual(a, [1, 2])

        a.pop_back()
        self.assertEqual(a, [1])

        a.pop_back()
        self.assertEqual(a, [])

        with self.assertRaises(ValueError):
            a.pop_back()

    def test_pop_front(self):
        a = sol.List.from_iterable([1, 2, 3])
        self.assertEqual(a, [1, 2, 3])

        a.pop_front()
        self.assertEqual(a, [2, 3])

        a.pop_front()
        self.assertEqual(a, [3])

        a.pop_front()
        self.assertEqual(a, [])

        with self.assertRaises(ValueError):
            a.pop_front()

    def test_erase(self):
        a = sol.List()
        self.assertEqual(a, [])

        a.erase(1)
        self.assertEqual(a, [])

        a = sol.List.from_iterable([1, 2, 3, 3, 3, 5])
        self.assertEqual(a, [1, 2, 3, 3, 3, 5])

        a.erase(3)
        self.assertEqual(a, [1, 2, 5])

        a.erase(4)
        self.assertEqual(a, [1, 2, 5])

    def test_forward_iteration(self):
        a = [1, 2, 3, 4, 5]
        b = sol.List.from_iterable(a)
        for item_in_a, item_in_b in zip(a, b):
            self.assertEqual(item_in_a, item_in_b)

    def test_backward_iteration(self):
        a = [1, 2, 3, 4, 5]
        b = sol.List.from_iterable(a)
        for item_in_a, item_in_b in zip(reversed(a), reversed(b)):
            self.assertEqual(item_in_a, item_in_b)

    def test_len(self):
        a = sol.List()
        self.assertEqual(len(a), 0)

        a.extend([1, 2, 3])
        self.assertEqual(len(a), 3)

    def test_contains(self):
        a = sol.List()
        self.assertFalse(1 in a)

        a.extend([1, 2, 3])
        self.assertTrue(1 in a)
        self.assertEqual(a, [1, 2, 3])

        self.assertTrue(2 in a)
        self.assertEqual(a, [1, 2, 3])

        self.assertTrue(3 in a)
        self.assertEqual(a, [1, 2, 3])

        self.assertFalse(4 in a)
        self.assertEqual(a, [1, 2, 3])


class TestMoveToFrontList(unittest.TestCase):
    def test_contains(self):
        a = sol.MoveToFrontList()
        self.assertFalse(1 in a)

        a.extend([1, 2, 3])
        self.assertTrue(1 in a)
        self.assertEqual(a, [1, 2, 3])

        self.assertTrue(2 in a)
        self.assertEqual(a, [2, 1, 3])

        self.assertTrue(3 in a)
        self.assertEqual(a, [3, 2, 1])

        self.assertFalse(4 in a)
        self.assertEqual(a, [3, 2, 1])


class TestTransposeList(unittest.TestCase):
    def test_contains(self):
        a = sol.TransposeList()
        self.assertFalse(1 in a)

        a.extend([1, 2, 3])
        self.assertTrue(1 in a)
        self.assertEqual(a, [1, 2, 3])

        self.assertTrue(2 in a)
        self.assertEqual(a, [2, 1, 3])

        self.assertTrue(3 in a)
        self.assertEqual(a, [2, 3, 1])

        self.assertFalse(4 in a)
        self.assertEqual(a, [2, 3, 1])


if __name__ == "__main__":
    unittest.main()
