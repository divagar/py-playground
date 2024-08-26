def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)

    print(start)

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

    return visited


if __name__ == '__main__':
    graph = {'0': ['1', '2'],
             '1': ['0', '3', '4'],
             '2': ['0'],
             '3': ['1'],
             '4': ['2', '3']}
    print("Following is Depth First Traversal: ")
    v = dfs(graph, '0')
    print(v)
