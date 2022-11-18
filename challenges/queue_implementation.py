# 1) implement a queue with 2 stacks
# 2) implement a queue recursively (stack + stack memory)

class TwoStackQueue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def is_empty(self):
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
            return True
        else:
            return False

    def enqueue(self, new_item):
        if len(self.dequeue_stack) != 0:
            while len(self.dequeue_stack) > 0:
                item = self.dequeue_stack.pop()
                self.enqueue_stack.append(item)

        self.enqueue_stack.append(new_item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("The queue is empty, cannot dequeue.")
        elif len(self.enqueue_stack) != 0:
            while len(self.enqueue_stack) > 0:
                item = self.enqueue_stack.pop()
                self.dequeue_stack.append(item)

        dequeued_item = self.dequeue_stack.pop()
        return dequeued_item

    def get_length(self):
        queue_length = len(self.dequeue_stack) + len(self.enqueue_stack)
        return queue_length


class RecursiveQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def enqueue(self, new_item):
        self.queue.append(new_item)

    def dequeue(self):

        if self.get_length() == 1:
            dequeued_item = self.queue.pop()
            return dequeued_item

        elif self.get_length() > 1:
            item = self.queue.pop()
            dequeing = self.dequeue()

        self.queue.append(item)

        return dequeing

    def get_length(self):
        return len(self.queue)
