def mat_to_list(adj_mat):
    """ Convert adjacency matrix to an adjacency list representation

    Parameters:
    -----------
    adj_mat : (a square 0-1 matrix)
        Adjacency matrix (n x n) of the graph (of n nodes)


    Returns:
    --------
     adj_list: `list[list[int]]`
        The adjacency list of the graph

    """
    converted_list_arr = []
    for i in range (len(adj_mat)):
        adj_list_arr = []
        for j in range (len(adj_mat)):
            if (adj_mat[i][j] == 1):
                adj_list_arr.append(j)
        converted_list_arr.append(adj_list_arr)

    return converted_list_arr