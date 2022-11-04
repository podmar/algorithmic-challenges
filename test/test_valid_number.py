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

# For example, all the following are valid numbers: ["-0.1", "+3.14", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

    def test_decimal_number(self):
        """ Tests if the solution works for decimal numbers
        """

        self.assertTrue(solution("4."))


if __name__ == "__main__":
    unittest.main()
