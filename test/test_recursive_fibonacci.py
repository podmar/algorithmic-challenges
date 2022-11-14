import unittest

from challenges.recursive_fibonacci import fib


class TestFibonacci(unittest.TestCase):
    def test_output_is_int(self):
        """Tests is the output is int
        """

        self.assertTrue(type(fib(3)) == int)

    def test_basic_cases(self):
        """ Testing for base cases not requiring recursion
        """

        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)

    def test_mid_range_numbers(self):
        """ Testing for mid range numbers
        """

        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(13), 233)

    def test_big_numbers(self):
        """ Testing for big numbers
        """

        self.assertEqual(fib(35), 9227465)  # ok
        # self.assertEqual(fib(53), 53316291173) # don't test, runtime too long in recursion
        # self.assertEqual(fib(100), 354224848179261915075) # don't test


if __name__ == "__main__":
    unittest.main()
