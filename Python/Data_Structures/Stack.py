class Stack(object):
    def __init__(self):
        self.stack = []

    def add(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return f"Stack is empty"

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return self.stack == []

    def clear(self):
        self.stack = []

    def print(self):
        return self.stack

    def size(self):
        return len(self.stack)

stack = Stack()
stack.add("A")
stack.add("B")
stack.add("C")
stack.add("D")
stack.add("E")

print(stack.print())
print(stack.peek())
#stack.clear()
print(stack.pop())
print(stack.isEmpty())
print(stack.print())