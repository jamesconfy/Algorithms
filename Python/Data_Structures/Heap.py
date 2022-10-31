import heapq

class Heap(object):
    def __init__(self, data=[]) -> None:
        self.heap = data
        heapq.heapify(self.heap)

    def push(self, data):
        heapq.heappush(self.heap, data)

    def remove(self):
        heapq.heappop(self.heap)

    def replace(self, data):
        heapq.heapreplace(self.heap, data)

    def poppush(self, data):
        heapq.heappushpop(self, data)

    def __str__(self) -> str:
        return f"{self.heap}"


data = Heap([2, 5, 4, 3, 10, 11, 9, 8, 7, 6, 1])
data.push(200)
data.push(100)
data.push(50)
data.push(20)
data.remove()
data.remove()
print(data)