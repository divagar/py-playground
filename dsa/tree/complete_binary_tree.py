class Tree:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def isCompleteBinaryTree(self):
		if(self.left is None and self.right is None):
			return True

		if(self.left is not None):
			return True