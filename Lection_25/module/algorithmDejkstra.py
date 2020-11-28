# ==================================================
#
#       Lection 25.
#       Algorithm Dijkstra
#       Поиск кратчайшего расстояния до вершины
# 
# ==================================================

from collections import deque

def main():
    # G = read_graph()
    # start = input("С какой вершины начать? \n")
    
    G = {'A': {'B': 2.0, 'H': 15.0}, 
         'B': {'A': 2.0, 'C': 1.0, 'D': 5.0}, 
         'C': {'B': 1.0, 'D': 3.0, 'F': 2.0, 'G': 1.0}, 
         'D': {'B': 5.0, 'C': 3.0, 'E': 6.0, 'F': 4.0}, 
         'E': {'D': 6.0, 'F': 7.0, 'I': 2.0}, 
         'F': {'C': 2.0, 'D': 4.0, 'E': 7.0,'G': 1.0, 'H': 3.0}, 
         'G': {'C': 1.0, 'F': 1.0}, 
         'H': {'A': 15.0, 'F': 3.0, 'I': 12.0}, 
         'I': {'E': 2.0, 'H': 12.0}}
    
    start = 'A'
    
    while start not in G:
        start = input("Такой вершины в графе нет. С какой вершины начать? \n")
    
    shortest_distances = dijkstra(G, start)
    # finish = input("К какой вершине построить путь?")    
    # while start not in G:
    #     start = input("Такой вершины в графе нет. К какой вершине построить путь?")
    
    # shortest_path = reveal_shortest_path(G, start, finish, shortest_distances)
    return shortest_distances
    

def read_graph():
    M = int(input("Введите количество ребер: "))    # M - количество ребер, далее - строки "A B вес"
    G = {}
    for i in range(M):
        a, b, weight = input("Введите параметры ребра - V1 V2 вес, через пробел: \n").split()
        weight = float(weight)
        add_edge(G, a, b, weight)
        add_edge(G, b, a, weight)

    return G

def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight
        
def dijkstra(G, start):
    Q = deque()
    S = {}
    S[start] = 0
    Q.append(start)

    while Q:
        v = Q.pop()
        for u in G[v]:
            if (u not in S or S[v] + G[v][u] < S[u]):
                S[u] = S[v] + G[v][u]
                Q.append(u)
                
    return S

shortest_distances = main()
print(shortest_distances, sep='\n')
###