import unittest

from challenges.rain_trap import solution


class TestRainWater(unittest.TestCase):
    def test_output_is_number(self):
        """Tests is the output is a number
        """

        self.assertTrue(type(solution([4, 1, 3, 1, 5])) == int)

    def test_output_value_positive_num(self):
        """ Tests is output correct when given only positive numbers
        """

        self.assertEqual(solution([4, 1, 3, 1, 5]), 7)
        self.assertEqual(solution([5, 1, 3, 1, 5]), 10)
        self.assertEqual(solution([4, 1, 3, 1, 0]), 2)
        self.assertEqual(solution([4, 0, 0, 0, 5]), 12)


if __name__ == "__main__":
    unittest.main()
