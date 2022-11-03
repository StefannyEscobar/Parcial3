#!/usr/bin/env python3
import math
import numpy as np
inf = math.inf
def FloydWarshall(grafo):
	for k in range(nodos):
		for i in range(nodos):
			for j in range(nodos):
				grafo[i][j] = min(grafo[i][j], grafo[i][k] + grafo[k][j])
	return np.array(grafo)

if __name__ == "__main__":
	grafo = [[0, 2, inf, inf, -1],
            [inf, 0, 1, inf, 4],
            [inf, inf, 0, 3, inf],
            [inf, inf, inf, 0, 7],
            [inf, inf, inf, inf, 0]]
	nodos = len(grafo)
	print(FloydWarshall(grafo))


