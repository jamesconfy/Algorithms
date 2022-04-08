class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    stack = []
    curr = root

    while True:
        if curr is not None:
            stack.append(curr)
            curr = curr.left

        elif stack:
            curr = stack.pop()
            print(curr.data, end=" ")
            curr = curr.right

        else:
            break

    print()


def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None


def postorder(root):
    if root is None:
        return

    ans = []
    stack = []

    while(True):
        while (root):
                # Push root's right child and then root to stack
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)

                # Set root as root's left child
            root = root.left

            # Pop an item from stack and set it as root
        root = stack.pop()

            # If the popped item has a right child and the
            # right child is not processed yet, then make sure
            # right child is processed before root
        if (root.right is not None and
                peek(stack) == root.right):
            stack.pop()  # Remove right child from stack
            stack.append(root)  # Push root back to stack
            root = root.right  # change root so that the
                # right childis processed next

            # Else print root's data and set root as None
        else:
            print(root.data, end=" ")
#            ans.append(root.data)
            root = None

        if (len(stack) <= 0):
            break
    print()

def preorder(root):
    if root is None:
        return

    stack = [root]
    while len(stack) > 0:
        curr = stack.pop()
        print(curr.data, end=" ")
        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)

    print()

def LeftView(root):
    if root is None:
        return []
    
    stack = [root]
    ans = []
    while stack:
        curr = stack.pop()
        ans.append(curr.data)
        if curr.left is not None:
            stack.append(curr.left)
            
        elif curr.left is None and curr.right is not None:
            stack.append(curr.right)
            
        else:
            break
            
    return ans


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.right = Tree(7)
root.right.left = Tree(6)

preorder(root)
inorder(root)
postorder(root)
