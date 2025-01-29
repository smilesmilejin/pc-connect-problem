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
