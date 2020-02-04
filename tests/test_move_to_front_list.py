import unittest
import doctest
import solists


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(solists.move_to_front_list))
    return tests


class TestMoveToFrontList(unittest.TestCase):
    def test_contains(self):
        a = solists.MoveToFrontList()
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
