from logging import NullHandler


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph():
    def __init__(self, size):
        self.size = size
        self.graph = [None] * size

    def add(self, v1, v2):
        n = Node(v2)
        n.next = self.graph[v1]
        self.graph[v1] = n

        # n = Node(v1)
        # n.next = self.graph[v2]
        # self.graph[v2] = n

    def print(self):
        for v in self.graph:
            print("Vertex :", v)
            n = v
            while n is not None:
                print(n.data)
                n = n.next


g = Graph(5)
g.add(0, 1)
g.add(0, 2)
g.add(0, 3)

g.add(1, 0)
g.add(1, 2)

g.add(2, 0)
g.add(2, 1)

g.add(3, 0)

g.print()