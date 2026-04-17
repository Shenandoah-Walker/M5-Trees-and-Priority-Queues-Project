#Stack constructor

class Stack:
    def __init__(self):
        self._stack = []
    def push(self, item):
        self._stack.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._stack.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._stack[-1]
    def is_empty(self):
        return len(self._stack) == 0
    def size(self):
        return len(self._stack)