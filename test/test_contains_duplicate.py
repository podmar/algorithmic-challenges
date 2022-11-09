import unittest

from challenges.contains_duplicate import solution


class TestContainsDuplicate(unittest.TestCase):
    def test_return_type(self):
        """Testing that the type of return value is boolean
        """

        self.assertTrue(isinstance(solution([1, 2, 3, 1]), bool))

    def test_duplicates(self):
        """Testing cases from the examples
        """

        self.assertEqual(solution([1, 2, 3, 1]), True)
        self.assertEqual(solution([1, 2, 3, 4]), False)
        self.assertEqual(solution([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)
        self.assertEqual(solution([1]), False)


if __name__ == "__main__":
    unittest.main()
