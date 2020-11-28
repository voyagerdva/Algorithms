# ==================================================
#
#       Lection 24.
#       Graph structure
#       servey - deep first search - ОБХОД ГРАФА В ГЛУБИНУ
# 
# ==================================================

from module import graph

G = {'a': set('b'), 
     'b': set('acd'), 
     'c': set('bd'), 
     'd': set('bc')}
G1 = {1: (2), 
      2: (1, 3, 4), 
      3: (2, 4), 
      4: (2, 3)}

graph = graph.Graph()

# graph.componentsQuantity(G)
graph.topSort(G)