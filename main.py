def next_moves(position, grid, visited):
    '''
    Given a (row, column) position, a grid of 1s and 0s, and a visited set
    returns a list of adjacent positions that have not been visited
    and have a value of 0
    '''

    # Holds each candidate position, changing the row or column by 1 or -1
    moves = (
        (position[0] + 1, position[1]),  # down
        (position[0] - 1, position[1]),  # up
        (position[0], position[1] + 1),  # right
        (position[0], position[1] - 1),  # left
    )

    possible = []

    # For each candidate move
    for row, column in moves:
        # Check that it's in-bounds, has a value of 0 and has not been visited
        if (0 <= row < len(grid) 
            and 0 <= column < len(grid[0])
            and grid[row][column] == 0
            and (row, column) not in visited):
            # If it satisfies all the requirements, it's a possible move
            possible.append((row, column))

    return possible


def biggest_group_size(grid):
    # Set to hold all the (row, column) positions that have been visited
    # Visited set is shared across all searches
    visited = set()

    def search(position):
        '''
        Perform a DFS starting at the given (row, column) position
        Return a count of how many non-visited connected 0s there are from that start
        '''
        # Add position so we don't visit it again
        visited.add(position)
        # Start count at 1 for the position we currently occupy
        count = 1
        # Find all the places we can go next
        moves = next_moves(position, grid, visited)
        
        # Recurse through all the possible moves
        for move in moves:
            # Do not recurse through positions that have already been visited
            if move not in visited:
                # Add the amount of 0s that were found from that search
                count += search(move)
        return count

    # The size off the biggest group we've found so far
    best_size = 0

    # Iterate over every position in the grid
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            # Store the position as a tuple
            position = (row, column)
            
            # If this is a 0 and we haven't searched it before
            if position not in visited and grid[row][column] == 0:
                # Perform a search to find the size of the group
                size = search(position)
                # Update the size if bigger than the best we've seen so far
                if size > best_size:
                    best_size = size
    return best_size


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

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
