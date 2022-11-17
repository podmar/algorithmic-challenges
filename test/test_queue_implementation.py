import unittest

from challenges.queue_implementation import TwoStackQueue, RecursiveQueue


class TestTwoStackQueue(unittest.TestCase):
    def setUp(self):
        self.queue = TwoStackQueue()
        self.queue.enqueue(19)
        self.queue.dequeue()
        self.queue.enqueue(1)
        self.queue.enqueue(14)

    def test_all_methods(self):
        """Tests is output of enqueue/ dequeue, is_empty, get_genth is correct
        """

        # self.assertEqual(self.queue.dequeue(), 14)
        # self.assertEqual(self.queue.get_length, 1)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertTrue(self.queue.is_empty())
        self.assertRaises(Exception, self.queue.dequeue())


if __name__ == "__main__":
    unittest.main()
