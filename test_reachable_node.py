import unittest
from reachable_node import reachable

class TestMapToList(unittest.TestCase):
    def test_reachable_node_example_1(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]

        adj_result = {3, 4}

        result = reachable(adj_list, 3)
        self.assertEqual(result, adj_result)

    def test_reachable_node_example_2(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]

        adj_result = {0, 1, 2, 3, 4}

        result = reachable(adj_list, 0)
        self.assertEqual(result, adj_result)

    def test_reachable_node_example_3(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]

        adj_result = {0, 1, 2, 3, 4}

        result = reachable(adj_list, 1)
        self.assertEqual(result, adj_result)

    def test_reachable_node_example_4(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]

        adj_result = {5}

        result = reachable(adj_list, 5)
        self.assertEqual(result, adj_result)

    def test_reachable_node_example_5(self):
        adj_list = [[1, 2], [3], [4, 5], [6], [7], [], [8], [7], []]

        adj_result = {0, 1, 2, 3, 4, 5, 6, 7, 8}

        result = reachable(adj_list, 0)
        self.assertEqual(result, adj_result)

    def test_reachable_node_example_6(self):
        adj_list = [[], [], [], [], []]

        adj_result = {0}

        result = reachable(adj_list, 0)
        self.assertEqual(result, adj_result)
        
    def test_reachable_node_example_7(self):
        adj_list = [[]]

        adj_result = {0}

        result = reachable(adj_list, 0)
        self.assertEqual(result, adj_result)
        
if __name__ == '__main__':
    unittest.main()