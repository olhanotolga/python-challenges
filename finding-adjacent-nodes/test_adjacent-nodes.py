def are_nodes_adjacent(node1, node2, matrix):
    # current_node_connections = matrix[node1]
    # sought_connection = current_node_connections[node2]
    # return bool(sought_connection)
    return bool(matrix[node1][node2])


def test_answer():
    matrix1 = [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]
    matrix2 = [
        [0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 1, 0],
    ]

    assert are_nodes_adjacent(0, 1, matrix1) == True
    assert are_nodes_adjacent(0, 2, matrix1) == False
    assert are_nodes_adjacent(0, 3, matrix2) == True
    assert are_nodes_adjacent(1, 4, matrix2) == False
    assert are_nodes_adjacent(3, 2, matrix2) == True
