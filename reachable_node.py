reachable_node = set()

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

    def reaching_node (adj_list, reachable_list, new_node, start_node):
        # if start node == current node break
        # if node already in set break
        # add to set
        # call the reach function
        
        if (new_node == start_node):
            return None
        
        for i in range (len(reachable_list)):
            if (reachable_list[i] in reachable_node):
                return None
            else:
                reachable_node.add(reachable_list[i])
                reaching_node(adj_list, adj_list[reachable_list[i]], reachable_list[i], start_node)
            
    current_node = adj_list[start_node]
    for i in range(len(current_node)):
        reachable_node.add(current_node[i])
        reaching_node (adj_list, adj_list[current_node[i]],current_node[i], start_node)
    return reachable_node

adj_list_1 = [[1, 3], [2], [0], [4], [3], []]

adj_result_1 = {3, 4}

result = reachable(adj_list_1, 3)
print (result)
print (result == adj_result_1)