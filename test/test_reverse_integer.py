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

    def test_solution_outside_32bit(self):
        """Testing if the solution returns 0 when number outside the 32 bit range
        """

        self.assertEqual(solution(21474836477), 0)
        self.assertEqual(solution(979769686877), 0)
        self.assertEqual(solution(-2147483670), 0)
        self.assertEqual(solution(-12345678765432), 0)

    def test_solution_32bit_inside_outside(self):
        """Testing if the solution returns correct value when the input inside but output outside 32 bit range
        """

        self.assertEqual(solution(-2147483648), 0)
        self.assertEqual(solution(2147483647), 0)
        self.assertEqual(solution(1563847412), 0)

# edge numbers: -2147483648, 2147483647


if __name__ == "__main__":
    unittest.main()
