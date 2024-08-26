class Graph():
    def __init__(self, size):
        self.size = size
        self.matrix = []
        for i in range(size):
            self.matrix.append([0 for i in range(size)])

    def add(self, v1, v2):
        if v1 == v2:
            print("Add: two vertex cant be same")
        else:
            self.matrix[v1][v2] = 1

    def remove(self, v1, v2):
        if v1 == v2:
            print("Remove: two vertex cant be same")
        else:
            self.matrix[v1][v2] = 0

    def print(self):
        print("printing...")
        for i in range(self.size):
            for j in range(self.size):
                print('{:4}'.format(self.matrix[i][j]))


g = Graph(5)
g.print()
g.add(1, 2)
g.add(1, 3)
g.print()
g.remove(1, 2)
g.print()
