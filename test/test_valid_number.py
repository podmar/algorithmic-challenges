import unittest

from challenges.valid_number import solution


class TestValidNumber(unittest.TestCase):
    def test_return_boolean(self):
        """Tests is the output is a boolean
        """

        self.assertTrue(isinstance(solution("2"), bool))

    def test_integer(self):
        """ Tests is the solution functions for integers
        """

        self.assertTrue(solution("2"))
        self.assertTrue(solution("-74"))
        self.assertTrue(solution("0089"))
        self.assertTrue(solution("0"))
        self.assertFalse(solution("abc"))
        self.assertFalse(solution("/('#122"))

    def test_decimal_number(self):
        """ Tests if the solution works for decimal numbers
        """

        self.assertTrue(solution("4."))
        self.assertTrue(solution("-0.1"))
        self.assertTrue(solution("+3.14"))
        self.assertTrue(solution("-.9"))

    def test_scientific_notation(self):
        """ Tests if the solution works for scientific notation
        """

        self.assertTrue(solution("2e10"))
        self.assertTrue(solution("-90E3"))
        self.assertTrue(solution("53.5e93"))
        self.assertTrue(solution("-123.456e789"))
        self.assertTrue(solution("+6e-1"))
        self.assertTrue(solution("3e+7"))

    def test_invalid_numbers(self):
        """ Tests if the solution works for invalid corner cases
        """
        self.assertFalse(solution("1a"))
        self.assertFalse(solution("--6"))
        self.assertFalse(solution("-+3"))
        self.assertFalse(solution("95a54e53"))
        self.assertFalse(solution("1e"))
        self.assertFalse(solution("e3"))
        self.assertFalse(solution("99e2.5"))


if __name__ == "__main__":
    unittest.main()
