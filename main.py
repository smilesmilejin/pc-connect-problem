def bfs_graph(grid, row_index, col_index, visited):
    """
    Return all connected zero-valued cells starting from the given index.

    Given a grid such as:

    grid = [
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
    ]

    Starting at (row_index = 0, col_index = 0), the function should return
    the connected component of zeros:

    [(0, 0), (0, 1), (0, 2),
    (1, 0), (1, 1), (1, 2)]

    The result should be the length of this list (in this example: 6).
    """

    current_visited = set()

    from collections import deque
    queue = deque()
    queue.append((row_index, col_index))

    while queue:
        current_row_index, current_col_index = queue.popleft()
        current_node = (current_row_index, current_col_index)

        if current_node in visited:
            continue

        visited.add(current_node)
        current_visited.add(current_node)

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

        for neighbor_row, neighbor_col in neighbors:
            if grid[neighbor_row][neighbor_col] == 0 and (neighbor_row, neighbor_col) not in visited:
                queue.append((neighbor_row, neighbor_col))

    return len(current_visited)


# Test bfs_graph

# grid = [
# [0, 0, 0, 1, 1],
# [0, 0, 0, 1, 1],
# [1, 1, 1, 0, 0],
# [1, 1, 1, 1, 0],
# [0, 0, 0, 1, 0],
# ]


# row_index = 0
# col_index = 0
# visited = set()

# print(bfs_graph(grid, row_index, col_index, visited))

# Expected connected region:
# (0,0), (0,1), (0,2), (1,0), (1,1), (1,2)
# Expected output length = 6


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

# Expected connected region:
# (2,3), (2,4), (3,4), (4,4)
# Expected output length = 4




def biggest_group_size(grid):
    visited = set()
    max_zeros = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0 and (row, col) not in visited:
                num_zeros = bfs_graph(grid, row, col, visited)
                max_zeros = max(num_zeros, max_zeros)

    return max_zeros


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

# Consider this scenario:
# The grid contains no zeros at all. Since there are no zero-valued
# cells, there are no connected zero regions. Therefore, the largest
# connected group size must be 0.

# grid = [
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
# ]

# assert biggest_group_size(grid) == 0
