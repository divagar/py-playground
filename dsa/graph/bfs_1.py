import collections


def bfs(graph, root):
    visited = []
    queue = collections.deque(graph[root])
    visited.append(root)

    while queue:
        vertex = queue.popleft()
        if not vertex in visited:
            visited.append(vertex)

        for next in graph[vertex]:
            if not next in queue and not next in visited:
                    queue.append(next)
    return visited

graph = {'0': ['1', '2', '3'],
         '1': ['0', '2'],
         '2': ['0', '1', '4'],
         '3': ['0'],
         '4': ['2']
         }

out = bfs(graph, '0')
print(out)
  