import unittest

from challenges.queue_implementation import TwoStackQueue, RecursiveQueue


class TestTwoStackQueue(unittest.TestCase):
    def setUp(self):
        self.queue = TwoStackQueue()
        self.queue.enqueue(19)
        self.queue.enqueue(1)
        self.queue.enqueue(14)

    def test_all_methods(self):
        """Tests is output of enqueue/ dequeue, is_empty, get_genth is correct for the 2 stack queue
        """

        self.assertEqual(self.queue.get_length(), 3)

        self.assertEqual(self.queue.dequeue(), 19)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 14)

        self.assertEqual(self.queue.get_length(), 0)

        self.queue.enqueue(32)
        self.assertEqual(self.queue.dequeue(), 32)
        self.assertTrue(self.queue.is_empty())

        self.queue.enqueue(0)
        self.queue.enqueue(3)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.dequeue(), 0)
        self.assertEqual(self.queue.dequeue(), 3)

        with self.assertRaises(Exception) as assert_error:
            self.queue.dequeue()
        self.assertEqual(
            assert_error.exception.args[0], "The queue is empty, cannot dequeue.")


if __name__ == "__main__":
    unittest.main()
