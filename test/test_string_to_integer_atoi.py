import unittest

from challenges.string_to_integer_atoi import solution

class TestStringToInteger(unittest.TestCase):
    def test_solution_basic(self):
        """Checking for basic test cases from task description
        """

        self.assertEqual(solution("42"), 42)
        self.assertEqual(solution("   -42"), -42)
        self.assertEqual(solution("4193 with words"), 4193)

    def test_solution_corner_cases(self):
        """Additional corner cases
        """
        self.assertEqual(solution("-0"), 0)
        self.assertEqual(solution("  +0"), 0)
        self.assertEqual(solution("  +47"), 47)
        self.assertEqual(solution("  + 47"), 0)
        self.assertEqual(solution("   this is no number string"), 0)
        self.assertEqual(solution("       -00091"), -91)

    def test_solution_32bit(self):
        """Testing results outside the lower min of the 32 bit range
        """
        self.assertEqual(solution("-214748364832423"), -2147483648)
        self.assertEqual(solution("  -214748364823324"), -2147483648)
        self.assertEqual(solution("-2357483648"), -2147483648)

    def test_solution_32bit(self):
        """Testing results outside of the max limit of the 32 bit range
        """
        self.assertEqual(solution("214748364832423"), 2147483647)
        self.assertEqual(solution("214748364823324"), 2147483647)
        self.assertEqual(solution("2357483648"), 2147483647)

if __name__ == "__main__":
    unittest.main()
