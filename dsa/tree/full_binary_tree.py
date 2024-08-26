class Tree:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def checkIsFullBinaryTree(self):
		if(self.left is None and self.right is None):
			return True
		if(self.left is not None and self.right is not None):
			return self.left.checkIsFullBinaryTree() and self.right.checkIsFullBinaryTree()
		return False


t = Tree(10)
print("Check is full binary tree")
print(t.checkIsFullBinaryTree())


t1 = Tree(10)
t1.left = Tree(20)
t1.right = Tree(30)
print("Check is full binary tree")
print(t1.checkIsFullBinaryTree())


t2 = Tree(10)
t2.left = Tree(20)
t2.right = Tree(30)
t2.left.left = Tree(40)
print("Check is full binary tree")
print(t2.checkIsFullBinaryTree())