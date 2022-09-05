import unittest

from challenges.dutch_national_flag import solution


class TestGap(unittest.TestCase):
    def test_output_type(self):
        """Testing the type of the output array
        """

        self.assertTrue(type(solution([0, 2, 0, 1, 2, 0, 1, 2, 0])) == list)

    def test_output_length(self):
        """Testing the lenght of the output array
        """

        self.assertEqual(len(solution([0, 2, 0, 1, 2, 0, 1, 2, 0])), 9)
        self.assertEqual(len(solution([0, 0, 0, 0, 0])), 5)
        self.assertEqual(len(solution([])), 0)
        self.assertEqual(len(solution([1, 1, 1, 1, 1, 1])), 6)

    def test_output_array(self):
        """Testing the expected output
        """

        self.assertEqual(solution([0, 1, 0]), [0, 0, 1])
        self.assertEqual(solution([1, 1, 0]), [0, 1, 1])
        self.assertEqual(solution([2, 1]), [1, 2])
        self.assertEqual(solution([0, 2, 0, 1, 2, 0, 1, 2, 0]), [
                         0, 0, 0, 0, 1, 1, 2, 2, 2])


if __name__ == "__main__":
    unittest.main()
