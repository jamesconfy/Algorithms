class Node:
    # Initiating 
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    # Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.data] + self.inorderTraversal(root.right)
    # Preorder traversal
    # Root -> Left -> Right
    def preorderTraversal(self, root):
        if not root:
            return []
        return [root.data] + self.preorderTraversal(root.left)  + self.preorderTraversal(root.right)
    # Postorder traversal
    # Left -> Rigft -> Root
    def postorderTraversal(self, root):
        if not root:
            return []
        return self.postorderTraversal(root.left)  + self.postorderTraversal(root.right) + [root.data]

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.PrintTree()
print(root.inorderTraversal(root))
print(root.preorderTraversal(root))
print(root.postorderTraversal(root))