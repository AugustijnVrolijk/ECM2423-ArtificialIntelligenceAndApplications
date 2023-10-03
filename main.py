from depthFirstSearch import depthFirstSearch
from Astar import AStar
import time
from supportFunctions import convertMazeTxt


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
        print("A* looked through {} nodes in {} seconds\nThe final solution was {} tiles long".format(AStarCount, Aruntime,
                                                                                                      Alength))
        print("\n---------------------------------------------------------------------------------------------------\n")


def main():
    mazes = ["../maze-Easy.txt", "../maze-Medium.txt", "../maze-Large.txt", "../maze-VLarge.txt"]
    for maze in mazes:
        SolveMaze(maze)


if __name__ == "__main__":
    main()
