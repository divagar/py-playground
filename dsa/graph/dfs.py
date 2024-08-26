
def dfs(graph, start, visited=None):
    if(visited is None):
        visited = set()
    visited.add(start)

    for nxt in (graph[start] - visited):
        dfs(graph, nxt, visited)
    return visited


graph = {'0': set(['1', '2', '3']), '1': set(['0', '2']), '2': set(
    ['0', '1', '4']), '3': set(['0']), '4': set(['2'])}
print("in ->", graph)
out = dfs(graph, '0')
print("out -> ", out)


graph = {0: set([1, 2, 3]), 1: set([0, 2]), 2: set(
    [0, 1, 4]), 3: set([0]), 4: set([2])}
print("in ->", graph)
out = dfs(graph, 0)
print("out -> ", out)
