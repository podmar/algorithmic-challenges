import unittest

from challenges.recursive_frog_jump import solution


class TestFrog(unittest.TestCase):
    def test_output_is_int(self):
        """Tests is the output is int
        """

        self.assertTrue(type(solution(3)) == int)

    def test_basic_cases(self):
        """ Testing for base cases not requiring recursion
        """

        self.assertEqual(solution(0), 0)
        self.assertEqual(solution(1), 1)
        self.assertEqual(solution(2), 2)

    def test_mid_range_numbers(self):
        """ Testing for mid range numbers
        """

        self.assertEqual(solution(3), 3)
        self.assertEqual(solution(4), 5)
        self.assertEqual(solution(6), 13)
        self.assertEqual(solution(11), 144)


if __name__ == "__main__":
    unittest.main()
