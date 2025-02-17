import unittest
from src.graph import Graph

class TestGraph(unittest.TestCase):
    def test_graph(self):
        list_of_decimal_values = [1.2, 2.4, 3.6, 4.8, 6.0]
        origin = (0, 0)
        graph = Graph(list_of_decimal_values)
        print(graph.cords())
        self.assertEqual(graph.cords(), graph.cords())



if __name__ == '__main__':
    unittest.main()
