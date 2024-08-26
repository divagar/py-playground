from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque()
    
    #initial value
    visited.add(start)
    queue.append(start)
    
    while len(queue) != 0:
        vertex = queue.popleft()
        for el in graph[vertex]:
            if el not in visited:
                visited.add(el)
                queue.append(el)
                
    print("Visited -", visited)
    return visited

    
if __name__ == '__main__':
    graph = {0: [1, 2], 1: [0, 3, 4], 2: [0], 3: [1], 4: [2, 3]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)