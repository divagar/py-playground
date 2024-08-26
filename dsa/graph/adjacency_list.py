class AdjacencyList:
	def __init__(self, data):
		self.vertex = data
		self.next = None

class Graph:
	def __init__(self, size):
		self.V = size
		self.graph = [None] * size

	def addEdge(self, v1, v2):
		node = AdjacencyList(v2)
		node.next = self.graph[v1]
		self.graph[v1] = node

		node = AdjacencyList(v1)
		node.next = self.graph[v2]
		self.graph[v2] = node

	def print(self):
		for i in range(self.V):
			print("i ->", i)
			print("Graph -> ", self.graph[i])
			t = self.graph[i]
			while t:
				print("->",t.vertex)
				t = t.next



g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(3, 0)

g.print()