# ==================================================
#
#       Lection 25.
#       Graph structure
#       bfs - breadth first search - ОБХОД ГРАФА В ШИРИНУ
# 
# ==================================================

from collections import deque

class Graph:
    def __init__(self):
        pass

    def dfs(self, graph, vertex, used):
        used.add(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in used:
                self.dfs(graph, neighbour, used)

    
    def componentsQuantity(self, graph):
        used = set()
        qty = 0

        for vertex in graph:
            if vertex not in used:
                self.dfs(graph, vertex, used)
                qty += 1
        print(qty)
        return qty
    
    
    def make(self):
        print("введите число вершин, число ребер и сами вершины будущего графа:")
        N, M = map(int, input().split())
    
        graph = {i: set() for i in range(N)}
        for i in range(M):
            v1, v2 = map(int, input().split())
            graph[v1].add(v2)
            graph[v2].add(v1)
        return graph
        

    def bfs(self, graph, N, M):
        distances = [None] * N
        start_vertex = 0
        distances[start_vertex] = 0
        queue = deque([start_vertex])

        while queue:
            cur_v = queue.popleft()
            for neigh_v in graph[cur_v]:
                if distances[neigh_v] is None:
                    distances[neigh_v] = distances[cur_v] + 1
                    queue.append(neigh_v)
        return distances

#############################################################

# G0 = {'a': set('b'), 'b': set('acd'), 'c': set('bd'), 'd': set('bc')}
# G1 = {1: 2, 2: (1, 3, 4), 3: (2, 4), 4: (2, 3)}
# gr = Graph()
# graph = gr.make()

N = 15 
M = 16
graph = {0: {1, 10, 11, 12}, 1: {0, 6, 7}, 2: set(), 3: {11}, 4: {10}, 5: {8, 12}, 6: {1, 10}, 7: {1, 13}, 8: {12, 5}, 9: {11}, 10: {0, 4, 6}, 11: {0, 3, 9, 12, 14}, 12: {0, 8, 11, 5}, 13: {7}, 14: {11}}

gr = Graph()
dist = gr.bfs(graph, N, M)
print(dist)