class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def inOrder(root):
    if root:
        inOrder(root.left)
        print(str(root.val))
        inOrder(root.right)


def preOrder(root):
    if root:
        print(str(root.val))
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(str(root.val))


myRoot = Node(10)
myRoot.left = Node(15)
myRoot.right = Node(20)
myRoot.left.left = Node(25)
myRoot.right.right = Node(30)

print("In order tree traversal")
inOrder(myRoot)

print("Pre order tree traversal")
preOrder(myRoot)

print("Post order tree traversal")
postOrder(myRoot)
