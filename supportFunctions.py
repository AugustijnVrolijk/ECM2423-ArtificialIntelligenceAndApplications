def convertMazeTxt(filename):
    maze = []
    with open(filename, "r") as f:
        for line in f:
            fLine = line.translate(str.maketrans("", "", "\n "))  # remove whitespace and end of line characters from
            # read line
            if fLine == "":  # in case empty lines are added at the end of the file
                break
            maze.append([])  # create "lines" in array
            for cell in fLine:
                maze[-1].append(cell)  # add each item back into each line as separate column

    # Maze is put into Maze[Y][X] format, as the first attribute decides the line and the second the columns as its
    # easier to read from txt file this way
    start = None
    end = None
    for i in range(len(maze[0])):
        if maze[0][i] == "-":
            start = (0, i)  # coord are used as line, column - aka (inverted Y, X)
        if maze[-1][i] == "-":
            end = (len(maze) - 1, i)
    return maze, start, end


def convertCoordToXY(solution, maze):
    Height = len(maze) - 1
    solutionXY = []
    for coord in solution:
        solutionXY.append((coord[1], Height - coord[0]))
    return solutionXY

def tester():
    maze, start, end = convertMazeTxt("../maze-VLarge.txt")
    columnWidth, lineHeight = len(maze[0]), len(maze)
    forks = 0
    for line in range(len(maze)):
        for column in range(len(maze[line])):
            count = 0
            if maze[line][column] == "#":
                continue
            for direction in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                lineTest = line + direction[0]
                columnTest = column + direction[1]
                if lineTest >= lineHeight or columnTest >= columnWidth or lineTest < 0 or columnTest < 0:
                    continue
                if maze[lineTest][columnTest] == "#":
                    continue
                count += 1
                if count == 3:
                    forks += 1
                    break
    print(forks)
    return

tester()