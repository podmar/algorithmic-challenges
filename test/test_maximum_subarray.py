import unittest

from challenges.maximum_subarray import solution


class TestContainsDuplicate(unittest.TestCase):
    def test_return_type(self):
        """Testing that the type of return value is boolean
        """

        self.assertTrue(isinstance(solution([1, 2, 3, 1]), int))

    def test_max_subarray(self):
        """Testing cases from the examples
        """

        self.assertEqual(solution([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(solution([1]), 1)
        self.assertEqual(solution([5, 4, -1, 7, 8]), 23)


if __name__ == "__main__":
    unittest.main()
