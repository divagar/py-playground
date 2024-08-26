class Tree:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def calculateHeight(self):
		l = 0
		r = 0
		
		if(self.left is None and self.right is None):
			return 0

		if(self.left):
			l = self.left.calculateHeight()
		if(self.right):
			r = self.right.calculateHeight()
		if(l > r):
			return (l+1)
		else:
			return (r+1)

	def calculateDepth(self):
		d = 1
		node = self.left
		while(node is not None):
			d += 1
			node = node.left
		return d

	def checkPerfectBinaryTree(self, depth, level = 0):
		if(self.left is None and self.right is None):
			return (depth == level + 1 )
		if(self.left is None or self.right is None):
			return False
		
		return self.left.checkPerfectBinaryTree(depth, level+1) and self.right.checkPerfectBinaryTree(depth, level+1)

t1 = Tree(10)
print("Height => ",  t1.calculateHeight())
print("Depth/level => ",  t1.calculateDepth())
print("Check the tree is a perfect binary tree")
print(t1.checkPerfectBinaryTree(t1.calculateDepth()))


t2 = Tree(10)
t2.left = Tree(20)
t2.right = Tree(30)
print("Height => ",  t2.calculateHeight())
print("Depth/level => ",  t2.calculateDepth())
print("Check the tree is a perfect binary tree")
print(t2.checkPerfectBinaryTree(t2.calculateDepth()))


t3 = Tree(10)
t3.left = Tree(20)
t3.right = Tree(30)
t3.left.left = Tree(40)
print("Height => ",  t3.calculateHeight())
print("Depth/level => ",  t3.calculateDepth())
print("Check the tree is a perfect binary tree")
print(t3.checkPerfectBinaryTree(t3.calculateDepth()))


t4 = Tree(10)
t4.left = Tree(20)
t4.right = Tree(30)
t4.left.left = Tree(40)
t4.left.right = Tree(50)
print("Height => ",  t4.calculateHeight())
print("Depth/level => ",  t4.calculateDepth())
print("Check the tree is a perfect binary tree")
print(t3.checkPerfectBinaryTree(t4.calculateDepth()))