import unittest

from challenges.max_in_stack import StackWithMaxValue


class TestMaxInStackOneValue(unittest.TestCase):
    def setUp(self):
        self.stack = StackWithMaxValue()
        self.stack.push(14)

    def test_output_is_int(self):
        """Tests is the output is int
        """

        self.assertIsInstance(self.stack.peek_max_value(), int)

    def test_stack_len(self):
        """ Testing stack lenth
        """
        self.assertEqual(self.stack.get_length(), 1)

    def test_max_value(self):
        """ Testing max value
        """
        self.assertEqual(self.stack.peek_max_value(), 14)

    def test_popping(self):
        """ Testing popping
        """
        self.assertEqual(self.stack.pop(), 14)
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.peek_max_value(), "Stack is empty")
        self.assertEqual(self.stack.get_length(), 0)


class TestMaxInStackMultipleOperations(unittest.TestCase):
    def setUp(self):
        self.stack = StackWithMaxValue()
        self.stack.push(14)
        self.stack.push(50)
        self.stack.pop()
        self.stack.push(0)
        self.stack.push(17)

    def test_stack_len(self):
        """ Testing stack lenth
        """
        self.assertEqual(self.stack.get_length(), 3)

    def test_max_value(self):
        """ Testing max value
        """
        self.assertEqual(self.stack.peek_max_value(), 17)

    def test_popping(self):
        """ Testing popping
        """
        self.assertEqual(self.stack.pop(), 17)
        self.assertEqual(self.stack.peek_max_value(), 14)
        self.assertEqual(self.stack.get_length(), 2)
        self.assertEqual(self.stack.pop(), 0)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.pop(), 14)
        self.assertTrue(self.stack.is_empty())


if __name__ == "__main__":
    unittest.main()
