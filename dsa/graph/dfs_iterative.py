
# def DFS(graph, root):
#     visited = set()
#     stack = [root]
#     visited.add(root)

#     while stack:
#         vertex = stack.pop()
#         for i in graph[vertex]:
#             if i not in visited:
#                 visited.add(i)
#                 stack.append(i)
#     print("visited -> ", visited)
#     print("stack -> ", stack)


# graph = {0: [1, 2], 1: [0, 3, 4], 2: [0], 3: [1], 4: [2, 3]}
# print("Graph -> ", graph)
# print("Depth First Search")
# DFS(graph, 0)


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

print(dfs(graph, '0'))
