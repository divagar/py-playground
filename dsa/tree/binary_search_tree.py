class Tree:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data


def traversal(node):
	if(node is not None):
		traversal(node.left)
		print(node.data)
		traversal(node.right)

def isBST(node, low=float('-inf'), high=float('inf')):
	if(node is None):
		return True
	if(node.data < low or node.data > high):
		return False
	return ((isBST(node.left, low, node.data)) and (isBST(node.right, node.data, high)))

t = Tree(10)
t.left = Tree(1)
t.right = Tree(20)
traversal(t)
print("isBST -> ", isBST(t))