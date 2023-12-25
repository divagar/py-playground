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

        print("Maze")
        print(maze)
        return maze
    except OSError as e:
        print("unknown error occurred while reading the maze |", e)
    finally:
        print("Done")

maze = readMaze("stack/maze_1.txt")
for row in maze:
    print(row)