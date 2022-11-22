import unittest

from challenges.two_sum import solution


class TestTwoSum(unittest.TestCase):

    def test_happy_path(self):
        """Testing the base cases from the example
        """
        self.assertEqual(solution([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(solution([3, 2, 4], 6), [1, 2])
        self.assertEqual(solution([3, 3], 6), [0, 1])

    def test_corner_cases(self):
        """Additional corner cases
        """
        self.assertEqual(solution([15, 7, 11, 2], 9), [1, 3])
        self.assertEqual(solution([3, 2, 0, 5, 4], 6), [1, 2])
        self.assertEqual(solution([3, 5, 6, 7, 3], 6), [0, 4])


if __name__ == "__main__":
    unittest.main()
