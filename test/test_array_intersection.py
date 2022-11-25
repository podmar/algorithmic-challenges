import unittest

from challenges.array_intersection import solution


class TestArrayIntersection(unittest.TestCase):

    def test_happy_path(self):
        """Testing the base cases from the example
        """
        self.assertEqual(solution([], []), [])


if __name__ == "__main__":
    unittest.main()
