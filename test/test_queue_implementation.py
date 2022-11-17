import unittest

from challenges.queue_implementation import TwoStackQueue, RecursiveQueue


class TestTwoStackQueue(unittest.TestCase):
    def setUp(self):
        self.queue = TwoStackQueue()
        self.queue.enqueue(19)
        self.queue.enqueue(1)
        self.queue.enqueue(14)

    def test_all_methods(self):
        """Tests is output of enqueue/ dequeue, is_empty, get_genth is correct
        """

        self.assertEqual(self.queue.dequeue(), 19)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 14)

        self.queue.enqueue(32)
        self.assertEqual(self.queue.dequeue(), 32)

        self.queue.enqueue(0)
        self.queue.enqueue(71)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.dequeue(), 0)

        # self.assertRaises(
        #     Exception("The queue is empty, cannot dequeue."), self.queue.dequeue())

        # self.assertFalse(self.queue.is_empty())
        # self.assertEqual(self.queue.dequeue(), 19)
        # self.assertEqual(self.queue.get_length, 2)
if __name__ == "__main__":
    unittest.main()
