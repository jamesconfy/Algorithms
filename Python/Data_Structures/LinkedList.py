class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        new_node = Node(new_data)
        temp = self.head
        while temp:
            if temp.data == prev_node:
                new_node.next = temp.next
                temp.next = new_node
                return

            temp = temp.next

        print(f"Node value {prev_node} is not in the Linked List")
        return

    def addEnd(self, new_data):
        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def removeNode(self, Removekey):
        headVal = self.head

        if (headVal is not None):
            if (headVal.data == Removekey):
                self.head = headVal.next
                headVal = None
                return

        while (headVal is not None):
            if headVal.data == Removekey:
                break
            prev = headVal
            headVal = headVal.next

        if headVal == None:
            return

        prev.next = headVal.next
        headVal = None

    def printList(self):
        temp = self.head
        res = ""

        while temp is not None:
            if temp.next is None:
                res += f"{temp.data}"
            else:
                res += f"{temp.data} => "
            temp = temp.next

        return res


# Start with the empty list
llist = LinkedList()

llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(3)
llist.addEnd(10)
llist.removeNode(7)
llist.insertAfter(3, 4)
llist.insertAfter(4, 5)
llist.insertAfter(14, 4)
llist.removeNode(20)

print('Created list is:', llist.printList())
