import unittest

from challenges.longest_substring import solution


class TestLongestSubstring(unittest.TestCase):
    def test_output_type(self):
        """Testing if the output is an integer.
        """

        self.assertTrue(type(solution("abc")) == int)

    def test_string_lenght(self):
        """Testing if the output is an integer.
        """

        self.assertEqual(solution("abc"), 3)
        self.assertEqual(solution("abacaba"), 2)
        self.assertEqual(solution("abcde"), 5)


if __name__ == "__main__":
    unittest.main()
