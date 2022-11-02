import unittest

from challenges.reverse_integer import solution


class TestReverseInteger(unittest.TestCase):
    def test_solution_positive(self):
        """Testing reversed positive integers
        """

        self.assertEqual(solution(123), 321)
        self.assertEqual(solution(120), 21)
        self.assertEqual(solution(445533), 335544)

    def test_solution_negative(self):
        """Testing the solution with negative numbers
        """
        self.assertEqual(solution(-123), -321)
        self.assertEqual(solution(-120), -21)
        self.assertEqual(solution(-5), -5)
        self.assertEqual(solution(-121), -121)

    def test_solution(self):
        """XX
        """


if __name__ == "__main__":
    unittest.main()
