#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island in the given grid.

    Parameters:
    grid (list of list of int): A 2D list representing the map.
                                0 represents water, 1 represents land.

    Returns:
    int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Start with 4 sides
                perimeter += 4

                # Check adjacent cells and subtract shared edges
                if r > 0 and grid[r - 1][c] == 1:  # Check top
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:  # Check left
                    perimeter -= 2

    return perimeter
