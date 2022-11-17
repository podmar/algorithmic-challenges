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
                self.equeue_stack.append(item)
        self.equeue_stack.append(new_item)

    def dequeue(self):
        return


class RecursiveQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
