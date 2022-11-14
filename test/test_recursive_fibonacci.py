import unittest

from challenges.recursive_fibonacci import solution


class TestFibonacci(unittest.TestCase):
    def test_output_is_int(self):
        """Tests is the output is int
        """

        self.assertTrue(type(solution(3)) == int)

    def test_(self):
        """ 
        """


if __name__ == "__main__":
    unittest.main()
