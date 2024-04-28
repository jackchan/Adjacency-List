import unittest
from mat_to_list import mat_to_list

class TestMapToList(unittest.TestCase):
    def test_mat_example_1(self):
        adj_mat =   [[0, 1, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0]]

        adj_list = [[1, 3], [2], [0], [4], [3], []]

        result = mat_to_list(adj_mat)
        self.assertEqual(result, adj_list)

    def test_mat_example_2(self):
        adj_mat = [[0, 1, 0],
                [0, 0, 1],
                [1, 0, 0]]

        adj_list = [[1], [2], [0]]

        result = mat_to_list(adj_mat)
        self.assertEqual(result, adj_list)

    def test_mat_example_3(self):
        adj_mat = [[0, 1, 1],
           [1, 0, 1],
           [0, 0, 0]]

        adj_list = [[1, 2], [0, 2], []]

        result = mat_to_list(adj_mat)
        self.assertEqual(result, adj_list)

    def test_mat_example_4(self):
        adj_mat = [[0, 1, 1, 1],
                [1, 0, 1, 1],
                [1, 1, 0, 1],
                [1, 1, 1, 0]]

        adj_list = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]

        result = mat_to_list(adj_mat)
        self.assertEqual(result, adj_list)

    def test_mat_example_5(self):
        adj_mat = [[0, 1],
                [1, 0]]

        adj_list = [[1], [0]]

        result = mat_to_list(adj_mat)
        self.assertEqual(result, adj_list)

    def test_mat_example_6(self):
        adj_mat = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        adj_list = [[], [], []]

        result = mat_to_list(adj_mat)
        self.assertEqual(result, adj_list)

if __name__ == '__main__':
    unittest.main()