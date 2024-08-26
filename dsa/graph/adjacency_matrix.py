class Graph:
	def __init__(self, size):
		self.size = size
		self.adjaMatrix = []
		for i in range(size):
			self.adjaMatrix.append([0 for i in range(size)])
		print("init -> ", self.adjaMatrix)

	def len(self):
		return self.size

	def print(self):
		print("printing the content")
		for row in self.adjaMatrix:
			for val in row:
				print(val)
			print

	def add(self, v1, v2):
		if(v1 == v2):
			print("Vertex are same")
		self.adjaMatrix[v1][v2] = 1
		self.adjaMatrix[v2][v1] = 1

	def remove(self, v1, v2):
		if(self.adjaMatrix[v1][v2] == 0):
			print("No edge connecting the vertex")
		self.adjaMatrix[v1][v2] = 0
		self.adjaMatrix[v2][v1] = 0


g = Graph(4)
g.print()

g.add(0, 1)
g.add(0, 2)
g.add(0, 3)
g.add(1, 0)
g.add(1, 2)
g.add(2, 0)
g.add(2, 1)
g.add(3, 0)
g.print()