class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


def insert(node, val):
    if node is None:
        return Node(val)

    if val < node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)

    return node


def delete(node, val):
    if node is None:
        return node

    if val < node.val:
        node.left = delete(node.left, val)
    elif val > node.val:
        node.right = delete(node.right, val)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        node.val = minValue(node.right)
        node.right = delete(node.right, node.val)

    return node


def minValue(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.val

def maxValue(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.val


def inOrder(root):
    if root is None:
        return None

    if root.left != None:
        inOrder(root.left)

    print(str(root.val) + " -> ", end="")

    if root.right != None:
        inOrder(root.right)


root = insert(None, 8)
insert(root, 3)
insert(root, 10)
insert(root, 1)
insert(root, 14)
insert(root, 6)
insert(root, 7)
insert(root, 4)

print("\nInOrder Traversal")
inOrder(root)

print("\nDeleting node with val 8")
delete(root, 8)

print("\nInOrder Traversal")
inOrder(root)
