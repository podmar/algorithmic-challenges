import unittest

from challenges.merge_sorted_array import solution


class TestMergeSortedArray(unittest.TestCase):
    def test_output_is_none(self):
        """Tests is the output is None
        """

        self.assertTrue(type(solution([4, 1, 3, 1, 5])) == None)

    def test_(self):
        """ 
        """


if __name__ == "__main__":
    unittest.main()
