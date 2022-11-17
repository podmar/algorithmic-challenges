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
                print(f"moving {item} to the enqueue stack")
                self.enqueue_stack.append(item)

        print(f"Current enqueue stack: {self.enqueue_stack}")
        self.enqueue_stack.append(new_item)
        print(
            f"Enque stack after appending {new_item} is: {self.enqueue_stack}")

    def dequeue(self):
        if self.is_empty():
            raise Exception("The queue is empty, cannot dequeue.")
        elif len(self.enqueue_stack) != 0:
            print("Dequeuing. items in enqueing stack, moving.")
            while len(self.enqueue_stack) > 0:
                item = self.enqueue_stack.pop()
                print(f"moving {item} to the dequeue stack")
                self.dequeue_stack.append(item)

        print(f"Current dequeue stack: {self.dequeue_stack}")
        dequeued_item = self.dequeue_stack.pop()
        print(
            f"Dequeue stack after dequeueing {dequeued_item} is: {self.dequeue_stack}")
        return dequeued_item

    def get_length(self):
        queue_length = max(self.enqueue_stack, self.dequeue_stack)
        return queue_length


class RecursiveQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
