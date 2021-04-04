def are_nodes_adjacent(node1, node2, matrix):
    """
    The function takes 3 arguments:

    - index of the first graph node (int)

    - index of the second graph node (int)

    - a node adjacency matrix (nested list).

    In the matrix, 1 indicates that a connection is true, and 0 indicates a connection is false.

    The function determines whether the given nodes are connected or not and returns a boolean.
    """
    # first node's connections with other nodes: matrix[node1]
    # first node's connection with the second node: matrix[node1][node2]
    # 0 and 1 are easily converted into boolean values:
    return bool(matrix[node1][node2])


def main():
    matrix1 = [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]
    answer1 = are_nodes_adjacent(0, 1, matrix1)
    answer2 = are_nodes_adjacent(0, 2, matrix1)
    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
