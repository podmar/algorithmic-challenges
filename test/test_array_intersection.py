import unittest

from challenges.array_intersection import solution


class TestArrayIntersection(unittest.TestCase):

    def test_result_type(self):
        """Testing the return type is an array
        """
        self.assertIsInstance(solution([], []), list)

    def test_happy_path(self):
        """Testing the base cases from the example
        """
        self.assertEqual(solution[1, 2, 2, 1], [2, 2], [2, 2])
        self.assertEqual(solution[4, 9, 5], [9, 4, 9, 8, 4], [4, 9])


if __name__ == "__main__":
    unittest.main()
