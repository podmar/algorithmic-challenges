import unittest

from challenges.max_in_stack import max_in_stack


class TestMaxInStackOutputType(unittest.TestCase):
    def setUp(self):
        self.stack

    def test_output_is_int(self):
        """Tests is the output is int
        """

        self.assertIsInstance(max_in_stack(self.stack), int)

    def test_happy_path(self):
        """ Testing first happy path case
        """


if __name__ == "__main__":
    unittest.main()
