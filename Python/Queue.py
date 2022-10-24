class Queue(object):
    def __init__(self):
        self.queue = []

    def add(self, data):
        self.queue.insert(0, data)

    def pop(self):
        if self.queue:
            return self.queue.pop()
        else:
            return f"Queue is empty"

    def peek(self):
        return self.queue[-1]

    def isEmpty(self):
        return self.queue == []

    def clear(self):
        self.queue = []

    def print(self):
        return self.queue

queue = Queue()
queue.add("A")
queue.add("B")
queue.add("C")
queue.add("D")
queue.add("E")

print(queue.print())
print(queue.peek())
#queue.clear()
print(queue.pop())
print(queue.isEmpty())
print(queue.print())