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

    def test_check_possibility_to_move(self):
        self.assertEqual(
            funcs.check_possibility_to_move([
                [2, 4, 8, 16],
                [4, 2, 16, 8],
                [2, 4, 8, 16],
                [4, 2, 16, 8]]),
            False)
        self.assertEqual(
            funcs.check_possibility_to_move([
                [2, 4, 8, 16],
                [2, 2, 16, 8],
                [2, 4, 8, 16],
                [4, 2, 16, 8]]),
            True)
if __name__ == '__main__':
    unittest.main()
