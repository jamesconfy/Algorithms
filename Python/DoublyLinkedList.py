class Node(object):
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None
    
class DoublyLinkedList(object):
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insertAfter(self, prev, data):
        if prev is None:
            return

        new_node = Node(data)
        temp = self.head
        while temp is not None:
            if temp.data == prev:
                new_node.next = temp.next
                temp.next = new_node
                new_node.prev = temp
                if new_node.next is not None:
                    new_node.next.prev = new_node
                return
            temp = temp.next

        print(f"Node value {prev} is not in the Linked List")
        return

    def addEnd(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        new_node.prev = last

    def removeNode(self, key):
        head = self.head

        if head is not None:
            if head.data == key:
                self.head = head.next
                self.head.prev = None
                head = None
                return

        while head is not None:
            if head.data == key:
                break
            prev = head
            head = head.next

        if head == None:
            return

        prev.next = head.next
        head.next.prev = prev
        head = None

    def printList(self):
        temp = self.head
        res = ""

        while temp is not None:
            if temp.next is None:
                res += f"{temp.data}"
            else:
                res += f"{temp.data} <=> "
            temp = temp.next

        return res

list = DoublyLinkedList()
list.push(6)
list.push(5)
list.push(3)
list.addEnd(7)
list.addEnd(8)
list.insertAfter(3, 4)
list.insertAfter(None, 4)
list.removeNode(15)
list.push(2)
list.push(1)
print(list.printList())