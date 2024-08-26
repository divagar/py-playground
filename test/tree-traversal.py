class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


def inOrder(root):
    if root != None:

        if root.left != None:
            inOrder(root.left)

        print(root.val, "-> ", end="")

        if root.right != None:
            inOrder(root.right)


def preOrder(root):
    if root != None:

        print(root.val, "-> ", end="")

        if root.left != None:
            preOrder(root.left)

        if root.right != None:
            preOrder(root.right)


def postOrder(root):
    if root != None:

        if root.left != None:
            preOrder(root.left)

        if root.right != None:
            preOrder(root.right)

        print(root.val, "-> ", end="")


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

print("\nInorder Traversal")
inOrder(root)
print("\nPreorder Traversal")
preOrder(root)
print("\nPostorder Traversal")
postOrder(root)
