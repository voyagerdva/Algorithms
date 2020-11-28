import unittest
from fixtureGraph import fixtureGraph as FX
from module import graph

class testGraph(unittest.TestCase):

    def test_checkComponentQty4Vertex(self):
        graph4V, qty = FX.fixtureCountCompQty4Vertex()
        myGraph = graph.Graph()
        qtyResult = myGraph.componentsQuantity(graph4V)
        self.assertEqual(qtyResult, qty)

    def test_checkComponentQty15Vertex(self):
        graph4V, qty = FX.fixtureCountCompQty15Vertex()
        myGraph = graph.Graph()
        qtyResult = myGraph.componentsQuantity(graph4V)
        self.assertEqual(qtyResult, qty)

if __name__ == '__main__':
    unittest.main()