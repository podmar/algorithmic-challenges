import unittest

from challenges.max_in_stack import StackWithMaxValue


class TestMaxInStackOutputType(unittest.TestCase):
    def setUp(self):
        self.stack = StackWithMaxValue()
        self.stack.push(14)

    def test_output_is_int(self):
        """Tests is the output is int
        """

        self.assertIsInstance(self.stack.peek_max_value(), int)

    def test_happy_path(self):
        """ Testing first happy path case
        """


if __name__ == "__main__":
    unittest.main()
