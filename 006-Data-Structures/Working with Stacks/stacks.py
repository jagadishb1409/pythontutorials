class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

      
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())  # Output: 3
s.pop()
print(s.peek())  # Output: 2
print(s.isEmpty())  # Output: False
s.pop()
s.pop()
print(s.isEmpty())  # Output: True
