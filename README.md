# Connect Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

We are interested in finding the size of largest group of connected zeroes in a square grid.

The matrix will consist of ones and zeroes. For example:

```py
grid = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
]
```

We notice that there are three groups of zeroes that are connected together. Zeroes are connected left, down, up, or right. They are NOT connected diagonally.

The largest of the three groups is the rectangle containing 6 zeroes in the top left corner. Thus, the size of the largest group is 6.

Write a function that takes in a square grid and returns the size of the largest group of zeroes.

## Examples

### Example 1

```py
grid = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
]
biggest_group_size(grid)
```

Produces

```py
6
```

### Example 2

```py
grid = [
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
]
biggest_group_size(grid)
```

Produces

```py
5
```

### Example 3

```py
grid = [
    [1, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1],
]
biggest_group_size(grid)
```

Produces

```py
20
```

### Example 4

```py
grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
biggest_group_size(grid)
```

Produces

```py
25
```

## Notes for the Interviewer

### Clarifying Questions

#### Q: What should I do if the input is smaller than 2x2?

A: You can assume the input will have at least 4 values

#### Q: Is it possible to have the height and width be different? Or a jagged array?

A: No. You are guaranteed the input will be square.

#### Q: What should I do if invalid input is passed in? Or if there is something other than 1 or 0 in the matrix?

A: You can assume that the input will be valid.

#### Q: Can zeroes be connected diagonally?

A: Nope.

#### Q: Can I mutate the input?

A: Yes.

### Hints

- If your candidate struggles with an initial algorithm, ask them what type of search algorithm would be helpful here. Either BFS or DFS can work! Have them talk through what needs to happen at each step of the search. Have them talk through the first example, and have them describe which positions would be visited in what order.

- If your candidate is unsure how to check every group, encourage them to first solve the simpler problem of finding the size of the group that starts at (0, 0). This will cause the first test to pass. If they finish that, they can return to how to find any group.

- If your candidate struggles to determine how to traverse the array, encourage them first to write a helper function similar to next_moves in the example. Once they have that working, they can use it in their search.

- Encourage your candidate to print the position at each step of the search if they are not passing the test cases and are unsure why. This can help debug the path that the search takes (and can be especially helpful for debugging infinite loops).

## Optional Bonus At-Home Challenges

To be attempted after completing the interview.

- What are the time/space complexities of the sample solution?

- The sample solution does not mutate the input. What would it look like if the input was mutated instead of using a visited set?

- If you wrote a solution that used DFS, try writing a solution that uses BFS or vice versa.

- If you wrote a solution that used recursion, try writing a solution that uses iteration or vice versa.

- Expand your solution so that it can handle non-square matrix inputs.

### Extra Hard

- Expand your solution so it can handle 3D input arrays. What about 4D? Or n-dimensional arrays?

- Suppose you are allowed to change a single position from a 1 to a 0. Write a program that determines the best position to flip so that the largest group size in the array is maximized.
