class Stack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def empty(self):
        return Stack.size(self) == 0

    def push(self, element):
        return self.data.append(element)

    def pop(self):
        if Stack.empty(self):
            print("Stack is empty")
        return self.data.pop()

    def peek(self):
        if Stack.empty(self):
            print("Stack is empty")
        return self.data[-1]


"""
from structs.stack import Stack

s = Stack()

s.push(1)
s.peek()
s.push(2)
s.peek()
"""
