def bfs_graph(grid, row_index, col_index):
    """
    return a complete index of connected zeros as a list


    grid = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    ]

    row_index = 0, col_index = 0

    result should be the length of [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

    """

    visited = set()
    # print('visted')

    from collections import deque

    queue = deque()

    queue.append((row_index, col_index))

    while queue:
        current_row_index, current_col_index = queue.popleft()
        current_node = (current_row_index, current_col_index)

        if current_node in visited:
            continue

        visited.add(current_node)

        # print('current_node', current_node)
        # print('visited', visited)

        neighbors = []

        # up, row - 1
        if current_row_index - 1 >= 0:
            neighbors.append((current_row_index-1, current_col_index))

        # down, row + 1
        if current_row_index + 1 <= len(grid) - 1:
            neighbors.append((current_row_index+1, current_col_index))

        # left, col - 1

        if current_col_index - 1 >= 0 :
            neighbors.append((current_row_index, current_col_index - 1))

        # right, col + 1
        if current_col_index + 1 <= len(grid[0]) - 1 :
            neighbors.append((current_row_index, current_col_index + 1))

        # print('neighbors: ', neighbors)

        for neighbor_row, neighbor_col in neighbors:
            if grid[neighbor_row][neighbor_col] == 0 and (neighbor_row, neighbor_col) not in visited:
                queue.append((neighbor_row, neighbor_col))

    #     print('queue: ', queue)

    # print('neighbors: ', neighbors)
    # print('visited:', visited)

    # print(list(visited))

    # return list(visited)

    return len(visited)


# grid = [
# [0, 0, 0, 1, 1],
# [0, 0, 0, 1, 1],
# [1, 1, 1, 0, 0],
# [1, 1, 1, 1, 0],
# [0, 0, 0, 1, 0],
# ]


# row_index = 0
# col_index = 0

# print(bfs_graph(grid, row_index, col_index))

# grid = [
# [0, 0, 0, 1, 1],
# [0, 0, 0, 1, 1],
# [1, 1, 1, 0, 0],
# [1, 1, 1, 1, 0],
# [0, 0, 0, 1, 0],
# ]


# row_index = 2
# col_index = 3

# print(bfs_graph(grid, row_index, col_index))





def biggest_group_size(grid):
    pass
    # visited = set() to tracked visited node (row, col)
    # create queues and add the first element
    # zeros_groups = [ [] ], each [] will a groups of connect 0 with index tuple (row, col)

    # loop through each element in the grid
        # if it is not visited and it is 0
            # traverse the graph function

                # graph_zeros = []

                # add the firsit element to the queue
                # while the queue is not empty:
                    # pop the first element from the queue
                    # add the elemnt to visited
                    # add it to graph_zeros
                    # check neighbors up, down, left, rights
                    # if neighbors are not out of index , and neighbors == 0
                        # add the neighbot to the queue

                # append graph_zeros to zeros_groups
    # return max(len(zeros_groups))

    # visited = set()

    # from collections import deque

    # queue = deque()

    # passs

    max_zeros = float('-inf')

    for row in range(len(grid)):
        # print('row: ', row)
        for col in range(len(grid[0])):
            # print('row: ', row)
            # print('col: ', col)

            # print(grid[row][col])
            if grid[row][col] == 0:
                # print(grid[row][col])
                num_zeros = bfs_graph(grid, row, col)
                max_zeros = max(num_zeros, max_zeros)

    return max_zeros

    # pass

grid = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
]
assert biggest_group_size(grid) == 6

grid = [
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
]
assert biggest_group_size(grid) == 5

grid = [
    [1, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1],
]
assert biggest_group_size(grid) == 20

grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
assert biggest_group_size(grid) == 25


grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
assert biggest_group_size(grid) == 25



print("All tests passed!")
print("Discuss time & space complexity if time remains.")

# Consider This Situation in the Future
# grid = [
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
# ]

# assert biggest_group_size(grid) == 0
