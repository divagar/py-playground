# search for char '7' from maze.txt using depth first search algo

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
    mazeRowLen = len(maze) - 1
    mazeColLen = len(maze[0]) - 1
    (neighborRow, neighborCol) = neighbor
    return neighborRow != -1 and neighborCol != -1 and neighborRow <= mazeRowLen and neighborCol <= mazeColLen and (not neighbor in visitedPath)

def dfs(maze, start, goal):
    found = 0
    searchList = [start]
    visitedPath = {start: None}
    try:
        while len(searchList) != 0 and not found:
            currentNode = searchList.pop()
            (currentRow, currentCol) = currentNode
            print("Current Node ->", currentNode)
            
            #get neighbor row,val
            print("Neighbor Nodes ->",)
            for direction in ["top", "right", "bottom", "left"]:
                (neighborOffsetRow, neighborOffsetCol) = neighoursOffsets[direction]
                neighbor = (currentRow + neighborOffsetRow, currentCol + neighborOffsetCol)
                if(isValidNode(maze, neighbor, visitedPath)):
                    print(neighbor)
                    searchList.append(neighbor)
                    visitedPath[neighbor] = currentNode
                if(neighbor == goal):
                    found = 1
                    break
    except OSError as e:
        print("Unknown error occurred while searching ", e)
    finally:
        print("Done searching")
        if(found):
            print("found the element in -> ", neighbor)
            print("visitedPath -> ", visitedPath)
            print("searchList -> ", searchList)

#read the maze
maze = readMaze("dfs/maze.txt")
print("maze")
for row in maze:
    print(row)

#search element in the maze
dfs(maze, (0,0), (3,3))