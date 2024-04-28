
def reachable(adj_list, start_node):
    """ Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node


    """
    reachable_node = set()
    
    for i in range (len(adj_list[start_node])):
        if (adj_list[start_node][i] in reachable_node):
            return None
        else:
            reachable_node.add(adj_list[start_node][i])
            reachable(adj_list, adj_list[start_node][i])
    
    if (len(reachable_node)==0): 
        reachable_node.add(start_node)

    return reachable_node

adj_list_1 = [[1, 3], [2], [0], [4], [3], []]

adj_result_1 = {3, 4}

result = reachable(adj_list_1, 1)
print (result)
print (result == adj_result_1)
