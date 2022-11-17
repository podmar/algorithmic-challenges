# design an algorithm that can return the maximum item of a stack in O(1) running time complexity. We can use O(N) extra memory!
# Hint: we can use another stack to track the max item!

class StackWithMaxValue:
    def __init__(self):
        self.stack = []
        self.max_values = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True

    def peek_max_value(self):
        if not self.is_empty():
            return self.max_values[- 1]
        else:
            return "Stack is empty"

    def push(self, value):
        if self.is_empty():
            self.max_values.append(value)
        else:
            self.max_values.append(max(value, self.max_values[- 1]))

        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            popped_value = self.stack[-1]
            self.stack = self.stack[:-1]
            self.max_values = self.max_values[:-1]
        else:
            popped_value = None
        return popped_value

    def get_length(self):
        return len(self.stack)
