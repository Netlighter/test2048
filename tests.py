import unittest
import funcs


class TestStringMethods(unittest.TestCase):
    def test_swipe_and_sum(self):
        self.assertEqual(
            funcs.swipe_and_sum([2, 8, 8, 2]),
            [2, 16, 2, 0])
        self.assertEqual(
            funcs.swipe_and_sum([0, 0, 2, 0]),
            [2, 0, 0, 0])
        self.assertEqual(
            funcs.swipe_and_sum([2, 0, 2, 0]),
            [4, 0, 0, 0])
        self.assertEqual(
            funcs.swipe_and_sum([0, 0, 4, 4]),
            [8, 0, 0, 0])

    def test_find_free_cells(self):
        self.assertEqual(
            funcs.find_free_cells([
                [0, 2, 3],
                [0, 5, 0],
                [2, 34, 5],
                [4, 3, 5]]),
            [[0, 0], [1, 0], [1, 2]])


if __name__ == '__main__':
    unittest.main()
