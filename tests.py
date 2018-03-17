import unittest
import funcs

class TestStringMethods(unittest.TestCase):
    def test_swipe_and_sum(self):
        self.assertEqual(
            funcs.swipe_and_sum([2, 8, 8, 2]),
            [2, 16, 2, 0])
        self.assertEqual(
            funcs.swipe_and_sum([0, 2, 0, 0]),
            [2, 0, 0, 0])

    def test_transpose_and_or_reverse(self):
        initial_matrix = [
            [2, 0, 2, 2],
            [2, 2, 0, 2],
            [2, 0, 2, 2],
            [0, 0, 0, 2]]
        need_to_transpose_field = True
        need_to_reverse_field = True


        self.assertEqual(
            list(funcs.transpose_and_or_reverse(
                funcs.transpose_and_or_reverse(initial_matrix,
                                               need_to_transpose_field,
                                               need_to_reverse_field)
                                               ),
                need_to_transpose_field,
                need_to_reverse_field),
            initial_matrix)


if __name__ == '__main__':
    unittest.main()
