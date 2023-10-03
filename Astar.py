import time
from queue import PriorityQueue
from supportFunctions import convertMazeTxt


def manhattanDistance(coord1, coord2):
    dist = abs(coord2[0] - coord1[0]) + abs(coord2[1] - coord1[1])
    return dist


def AStar(maze, start, end):
    columnWidth, lineHeight = len(maze[0]), len(maze)
    pq = PriorityQueue()  # format for queue additions is: (priority, (node), h heuristic ), h heuristic is number of
    # steps from the start node
    solution = {start: start}  # dictionary to show parent - child relations
    pq.put((manhattanDistance(start, end), start, 0))
    count = 0

    while pq.queue:
        current = pq.get()
        count += 1

        if current[1] == end:
            path = [end]
            oldTemp = current[1]
            while oldTemp is not start:  # backtrack through parent - child dictionary to get path from end node to the
                # start node
                newTemp = solution[oldTemp]
                path.append(newTemp)
                oldTemp = newTemp
            return path, count

        for direction in [(1, 0), (0, -1), (0, 1), (-1, 0)]:
            line = current[1][0] + direction[0]
            column = current[1][1] + direction[1]
            if line >= lineHeight or column >= columnWidth or line < 0 or column < 0:  # check potential coordinates are
                # in range
                continue
            h = current[2] + 1  # enables A* to have more accurate heuristic for half of the f value. As the distance
            # the current node to the end will be an estimation, at least the distance to the current node from the
            # start is accurate
            f = h + manhattanDistance(end, (line, column))
            if maze[line][column] == "#":
                continue
            if solution.get((line, column)):  # ensures solution dictionary entries are not re-written
                continue
            solution[(line, column)] = current[1]
            pq.put((f, (line, column), h))
    return None, 0


def SolveMaze(mazeName):
    maze, start, end = convertMazeTxt(mazeName)
    AstartTime = time.perf_counter()
    AStarSolution, AStarCount = AStar(maze, start, end)
    Alength = len(AStarSolution)
    AstopTime = time.perf_counter()
    Aruntime = AstopTime - AstartTime

    if AStarSolution is None:
        print("A* found no path for {}".format(mazeName.translate(str.maketrans("", "", ".txt/"))))
    else:
        print("A* solution for {} is\n{}".format(mazeName.translate(str.maketrans("", "", ".txt/")),
                                                 AStarSolution))
        print("A* looked through {} nodes in {} seconds\nThe final solution was {} tiles long\n".format(AStarCount,
                                                                                                      Aruntime,
                                                                                                      Alength))


def main():
    mazes = ["../maze-Easy.txt", "../maze-Medium.txt", "../maze-Large.txt", "../maze-VLarge.txt"]
    for maze in mazes:
        SolveMaze(maze)


if __name__ == "__main__":
    main()
