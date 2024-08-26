def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    if not start in visited:
        visited.append(start)

    for rest in list(set(graph[start]) - set(visited)):
        dfs(graph, rest, visited)
    return visited


graph = {'0': ['1', '2', '3'],
         '1': ['0', '2'],
         '2': ['0', '1', '4'],
         '3': ['0'],
         '4': ['2']
         }

out = dfs(graph, '0')
print(out)
  