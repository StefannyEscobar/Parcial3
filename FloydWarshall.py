#!/usr/bin/env python3
import math
import numpy as np
INF = math.inf

class FloydWarshall:
	def __init__(self, graph):
		self.V = len(graph)
		self.graph = graph

	def floyd_warshall(self):

		for k in range(self.V):
			for i in range(self.V):
				for j in range(self.V):
					self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])
		return self
	def printSolution(self):
		print(np.array(self.graph))



if __name__ == "__main__":
    graph = [[0, 2, INF, INF, -1],
            [INF, 0, 1, INF, 4],
            [INF, INF, 0, 3, INF],
            [INF, INF, INF, 0, 7],
            [INF, INF, INF, INF, 0]]
    FloydWarshall(graph).floyd_warshall().printSolution()


