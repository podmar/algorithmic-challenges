import unittest

from challenges.string_to_integer_atoi import solution

class TestStringToInteger(unittest.TestCase):
    def test_solution_basic(self):
        """Checking for basic test cases from task description
        """

        self.assertEqual(solution("42"), 42)
        self.assertEqual(solution("   -42"), -42)
        self.assertEqual(solution("4193 with words"), 4193)

if __name__ == "__main__":
    unittest.main()
