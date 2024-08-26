from collections import deque

def BFS(graph, root):
	visited = set()
	queue = deque([root])
	visited.add(root)

	while queue:
		print("---")
		print("visited ->", visited)
		print("queue ->", queue)
		vertex = queue.popleft()
		print("vertex ->", vertex)

		for i in graph[vertex]:
			if i not in visited:
				visited.add(i)
				queue.append(i)

graph = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1], 3: [0]}
print("Graph -> ", graph)
print("Breadth First Search")
BFS(graph, 0)