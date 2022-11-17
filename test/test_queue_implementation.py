import unittest

from challenges.queue_implementation import TwoStackQueue, RecursiveQueue


class TestTwoStackQueue(unittest.TestCase):
    def setUp(self):
        self.queue = TwoStackQueue()
        self.queue.enqueue(14)

    def test_pop_output(self):
        """Tests is the output of pop function is correct
        """

        self.assertIsInstance(self.queue.pop(), 14)


if __name__ == "__main__":
    unittest.main()
