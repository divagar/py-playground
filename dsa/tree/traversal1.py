class Tree:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def traverseInOrder(self):
		if(self.left):
			self.left.traverseInOrder()
		print(self.data)
		if(self.right):
			self.right.traverseInOrder()

	def traversePreOrder(self):
		print(self.data)
		if(self.left):
			self.left.traversePreOrder()
		if(self.right):
			self.right.traversePreOrder()

	def traversePostOrder(self):
		if(self.left):
			self.left.traversePostOrder()
		if(self.right):
			self.right.traversePostOrder()
		print(self.data)


t = Tree(30)
t.left = Tree(35)
t.right = Tree(40)
t.left.left = Tree(45)
t.left.right = Tree(50)
t.right.left = Tree(55)
t.right.right = Tree(60)

print("InOrder Traversal")
t.traverseInOrder()

print("PreOrder Traversal")
t.traversePreOrder()

print("PostOrder Traversal")
t.traversePostOrder()