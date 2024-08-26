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


def search(node, key):
	if(node is None):
		return None
	if(node.data == key):
		return node.data
	elif(node.data > key):
		return search(node.left, key)
	else:
		return search(node.right, key)

def findMinValueNode(node):
	if(node is not None):
		cur = node
		while(cur.left is not None):
			cur = cur.left
		return cur

def findMaxValueNode(node):
	if(node is not None):
		cur = node
		while(cur.right is not None):
			cur = cur.right
		return cur

def insert(node, key):
	if(node is not None):
		print("data -> ", node.data)
	if(node is None):
		print("insert")
		return Tree(key)
	if(node.data > key):
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)
	return node

def delete(node, key):
	if(node is None):
		return node
	if(node.data > key):
		node.left = delete(node.left, key)
	elif(node.data < key):
		node.right = delete(node.right, key)
	else:
		if(node.left is None):
			temp = node.right
			node = None
			return temp
		elif(node.right is None):
			temp = node.left
			node = None
			return temp

		temp = findMinValueNode(node.right)
		node.data = temp.data
		node.right = delete(node.right, temp.key)
	return node
		

t = Tree(10)
t.left = Tree(5)
t.right = Tree(20)

print("Traversal")
traversal(t)

print("search for 5")
print(search(t, 5))

print("insert for 11")
print(insert(t, 11))

print("Traversal")
traversal(t)

print("insert 1")
print(insert(t, 1))

print("Traversal")
traversal(t)

print("insert 15")
print(insert(t, 15))

print("Traversal")
traversal(t)

print("find min value node")
print(findMinValueNode(t).data)
print("find max value node")
print(findMaxValueNode(t).data)

print("Traversal")
traversal(t)

print("delete 10")
print(delete(t, 10))

print("Traversal")
traversal(t)