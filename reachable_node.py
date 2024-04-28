
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
    
    def reachable_search(node):
        for i in range (len(adj_list[node])):
            if (adj_list[node][i] in reachable_node):
                break
            else:
                reachable_node.add(adj_list[node][i])
                reachable_search(adj_list[node][i])
        
        reachable_node.add(node)
    
    reachable_search(start_node)
    return reachable_node