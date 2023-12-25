from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if(not self.isEmpty()):
            return self.items.popleft()
        
def readMaze(filename):
    maze = []
    try:
        with open(filename) as fp:
            for line in fp:
                list = []
                for el in line:
                    if not el == "\n":
                        list.append(el)
                maze.append(list)
        return maze
    except OSError as e:
        print("unknown error occurred while reading the maze |", e)
    finally:
        print("Done")

neighoursOffsets = {
    'right': (0, 1),
    'left': (0, -1),
    'top': (-1, 0),
    'bottom': (1, 0)
}

def isValidNode(maze, neighbor, visitedPath):
    mazeRowLen = len(maze)-1
    mazeColLen = len(maze[0])-1
    neighborRow, neighborCol = neighbor
    return neighborRow != -1 and neighborCol != -1 and neighborRow <= mazeRowLen and neighborCol <= mazeColLen and (not neighbor in visitedPath)

def bfs(maze, start, goal):
    found = 0;
    searchQueue = Queue()
    searchQueue.enqueue(start)
    visitedPath = {start: None}
    try:
        while (not searchQueue.isEmpty() and found == 0):
            currentNode = searchQueue.dequeue()
            currentNodeRow, currentNodeCol = currentNode
            print("Current Node ->", currentNode)

            #find all neighbors of current node
            print("Neighbor Node ->")
            for direction in ["top", "right", "bottom", "left"]:
                neighoursOffsetsRow, neighoursOffsetsCol = neighoursOffsets[direction]
                neighbor = (currentNodeRow + neighoursOffsetsRow, currentNodeCol + neighoursOffsetsCol)
                #check this neighbor is a valid one
                if(isValidNode(maze, neighbor, visitedPath)):
                    print(neighbor)
                    searchQueue.enqueue(neighbor)
                    visitedPath[neighbor] = currentNode
                if(neighbor == goal):
                    found = 1
                    break
    except OSError as e:
        print("Unknown error occurres during bfs ", e)
    finally:
        print("Done searching")
        if(found):
            print("found the element in -> ", neighbor)
            print("visitedPath -> ", visitedPath)
            print("searchList -> ", searchQueue.items)

#read the maze
maze = readMaze("bfs/maze.txt")
for row in maze:
    print(row)

#find the element using bfs algo
bfs(maze, (0,0), (3,3))
