class Node:
	def __init__(self, val=7):
		self.left = None
		self.val = val
		self.right = None

	def inOrderWalk(self, node):
		if(node):
			self.inOrderWalk(node.left)
			print("val -> ", node.val)
			self.inOrderWalk(node.right)

	def preOrderWalk(self, node):
		if(node):
			print("val -> ", node.val)
			self.preOrderWalk(node.left)
			self.preOrderWalk(node.right)

	def postOrderWalk(self, node):
		if(node):
			self.postOrderWalk(node.left)
			self.postOrderWalk(node.right)
			print("val -> ", node.val)


n = Node(10)
n.left = Node(11)
n.right = Node(12)

print("inOrderWalk")
n.inOrderWalk(n)

print("preOrderWalk")
n.preOrderWalk(n)

print("postOrderWalk")
n.postOrderWalk(n)
		