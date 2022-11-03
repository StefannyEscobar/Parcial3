#!/usr/bin/env python3
import math
import numpy as np
INF = math.inf



def floyd_warshall(graph):

	for k in range(V):
		for i in range(V):
			for j in range(V):
				graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
	return graph
def printSolution(graph):
	print(np.array(graph))



if __name__ == "__main__":
	graph = [[0, 2, INF, INF, -1],
            [INF, 0, 1, INF, 4],
            [INF, INF, 0, 3, INF],
            [INF, INF, INF, 0, 7],
            [INF, INF, INF, INF, 0]]
	V = len(graph)
	printSolution(floyd_warshall(graph))
