# ==================================================
#
#       Lection 24.
#       Graph structure
#       dfs - deep first search - ОБХОД ГРАФА В ГЛУБИНУ
# 
# ==================================================

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

#############################################################
    def dfsSort(self, graph, vertex, used, ans):
        used.add(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in used:
                self.dfsSort(graph, neighbour, used, ans)
        ans.append(vertex)
                

    def topSort(self, graph):
        used = set()
        qty = 0
        ans = []

        for vertex in graph:
            if vertex not in used:
                self.dfsSort(graph, vertex, used, ans)
                
        print(ans)
        return ans
#################################################################



    # def dfsSort(self, start, graph, visited, ans):
    #     visited[start] = True
    #     for i in graph[start]:
    #         if not visited[i]:
    #             self.dfsSort(i, graph, visited, ans)
    #     ans.append(start)

    # def topSort(self, graph):
    #     visited = [False] * (len(graph) + 1)
    #     ans = []
        
    #     for i in range(1, len(graph) + 1):
    #         if not visited[i]:
    #             self.dfsSort(i, graph, visited, ans)
        
    #     ans[:] = ans[::-1]
    #     print(ans)
    #     return ans




G = {'a': set('b'), 
     'b': set('acd'), 
     'c': set('bd'), 
     'd': set('bc')}
G1 = {1: 2, 
      2: (1, 3, 4), 
      3: (2, 4), 
      4: (2, 3)}

graph = Graph()

# graph.componentsQuantity(G)
graph.topSort(G)
