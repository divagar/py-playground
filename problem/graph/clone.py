import collections


def cloneGraph(graph, start):
    visited = []
    queue = collections.deque(graph(start))
    visited.append(start)

    while queue:
        vertex = queue.popleft()
        if not vertex in visited:
            visited.append(start)


input = {'a': ['b', 'c'],
         'b': ['a', 'd', 'e'],
         'c': ['a', 'd'],
         'd': ['b', 'c', 'e'],
         'e': ['b', 'd']}

output = cloneGraph(input, 'a')
