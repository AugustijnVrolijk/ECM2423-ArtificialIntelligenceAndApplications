import time
from supportFunctions import convertMazeTxt


def depthFirstSearch(maze, start, end):
    columnWidth, lineHeight = len(maze[0]), len(maze)
    stack = [(start, start)]  # format for stack additions is:  [Parent, child] - where parent and child is a tuple in
    # format (Y, X) Y is inverted
    solution = [start]  # solution starts with start to allow backtracking loop to work on first iteration of while
    # stack:
    count = 0
    while stack:
        current = stack.pop()
        count += 1

        while current[0] != solution[-1]:  # this checks if algorithm is backtracking - pops the last solution if its
            # backtracking
            solution.pop()
        solution.append(current[1])

        if current[1] == end:
            solution.pop(0)  # remove the initial start we added to solution
            return solution, count

        for direction in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
            line = current[1][0] + direction[0]
            column = current[1][1] + direction[1]
            if line >= lineHeight or column >= columnWidth or line < 0 or column < 0:  # check potential coordinates are
                # in range
                continue
            if maze[line][column] != "-":  # if tile at specific coord's is unexplored and a path
                continue
            maze[line][column] = "E"  # label the tile as E for explored - don't have to create a
            # separate array to store explored
            stack.append((current[1], (line, column)))

    return None, 0  # 0 mentioned as calling function expects a format of solution , count.


def SolveMaze(mazeName):
    maze, start, end = convertMazeTxt(mazeName)
    startTime = time.perf_counter()
    Solution, Count = depthFirstSearch(maze, start, end)
    length = len(Solution)
    stopTime = time.perf_counter()
    runTime = stopTime - startTime

    if Solution is None:
        print("Depth-First found no path for {}".format(mazeName.translate(str.maketrans("", "", ".txt/"))))
    else:
        print("Depth-First search solution for {} is\n{}".format(mazeName.translate(str.maketrans("", "", ".txt/")),
                                                                 Solution))
        print("Depth-First looked through {} nodes in {} seconds\nThe final solution was {} tiles long\n".format(Count,
                                                                                                                runTime,
                                                                                                                length))


def main():
    mazes = ["../maze-Easy.txt", "../maze-Medium.txt", "../maze-Large.txt", "../maze-VLarge.txt"]
    for maze in mazes:
        SolveMaze(maze)


if __name__ == "__main__":
    main()
