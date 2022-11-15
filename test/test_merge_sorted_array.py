import unittest

from challenges.merge_sorted_array import merge


class TestMergeSortedArray(unittest.TestCase):
    def setUp(self):
        self.nums1 = [1, 2, 3, 0, 0, 0]
        self.m = 3
        self.nums2 = [2, 5, 6]
        self.n = 3

    def test_output_is_none(self):
        """Tests is the output is None
        """

        self.assertIsNone(merge(self.nums1, self.m, self.nums2, self.n))

    def test_(self):
        """ Testing first happy path case
        """
        merge(self.nums1, self.m, self.nums2, self.n)
        self.assertEquals(self.nums1, [1, 2, 2, 3, 5, 6])


if __name__ == "__main__":
    unittest.main()
