import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []

    def put(self, item, priority):
        heapq.heappush(self.items, (priority, item))

    def get(self):
        return heapq.heappop(self.items)[1]
    
    def isEmpty(self):
        return not self.items
    
    def __str__(self):
        return str(self.items)

#test priority queue
'''
pq = PriorityQueue()

pq.put("eat", 3)
pq.put("sleep", 1)
pq.put("code", 2)
print(pq)

print(pq.get())
print(pq.get())
print(pq.get())
print(pq)
'''

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

neighboursOffsets = {
    'right': (0, 1),
    'left': (0, -1),
    'top': (-1, 0),
    'bottom': (1, 0)
}

def checkValidCell(maze, neighbor):
    mazeRow = len(maze)-1
    mazeCol = len(maze[0])-1
    neighborRow, neighborCol = neighbor

    return (neighborRow != -1 and neighborCol != -1 and neighborRow <= mazeRow and neighborCol <= mazeCol and maze[neighborRow][neighborCol] != "*")

def computeHeuristicValue(a, b):
    r1, c1 = a
    r2, c2 = b
    
    return (abs(r1-r2) + abs(c1-c2))

'''
What is a A* algorithm
G-value -> Distance from start to the current cell
H-value -> Heuristic distance from current cell to target/goal cell
F-value -> Sum of G and H values

#1 Calculate the F value of the current cell
#2 put start pos with F value to the priority queue ex: ((0,0), 2)
#3 get the highest priority item from priority queue
#4 check you are in goal position, if yes exit the flow
#5 calculate the neighbours with F value and add to the priority queue
#6 update the search path hash map
#7 repeat till the priority queue is empty
'''
def aStar(maze, startPos, GoalPos):
    reachedGoal = 0
    searchPQ = PriorityQueue()
    searchPath = {}
    gValues = {}
    try:
        searchPQ.put(startPos, 0)
        searchPath[startPos] = None
        gValues[startPos] = 0

        while not searchPQ.isEmpty():
            #get current cell
            print("\n",searchPQ)
            currentCell = searchPQ.get()
            print("currentCell -> ", currentCell)
            #get current cell' G value
            currentGvalue = gValues[currentCell]
            #check is this goal pos
            if(currentCell == GoalPos):
                reachedGoal = 1
                break
            #get the neighbours
            for directions in ["top", "right", "bottom", "left"]:
                neighbour = (neighboursOffsets[directions][0] + currentCell[0], neighboursOffsets[directions][1] + currentCell[1])
                if (checkValidCell(maze, neighbour)) and (not neighbour in searchPath):
                    #get G value
                    neighbourGvalue = currentGvalue + 1
                    #get H value
                    neighbourHvalue = computeHeuristicValue(GoalPos, neighbour)
                    #compute F value
                    neighbourFvalue =  neighbourGvalue + neighbourHvalue
                    print("Neighbour -> ", neighbour, "G ->", neighbourGvalue, "H ->", neighbourHvalue, "F ->", neighbourFvalue)
                    #put the neighbours to search pq
                    #searchPQ.put(neighbour, neighbourFvalue)
                    searchPQ.put(neighbour, neighbourHvalue)
                    searchPath[neighbour] = currentCell
                    gValues[neighbour] = neighbourGvalue
    except OSError as e:
        print("Unknown error occured while walking the maze using A* algo ", e)
    finally:
        print("Done searching")
        if reachedGoal:
            print("searchPath -> ", searchPath)
            print("searchList -> ", searchPQ)

#read the maze file
maze = readMaze("heap/maze.txt")
for row in maze:
    print(row)

#perform a* based maze search
aStar(maze, (0,0), (3,3))