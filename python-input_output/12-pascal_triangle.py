#!/usr/bin/python3
"""Module that generates Pascal's Triangle"""

def pascal_triangle(n):
    """Return a list of list of integer representing Pascal's triangle of n"""
    if n <= 0:
        return []
    
    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range (1, i):
            row.append(triangle[i-1][j-1])
            row.append(1)
            triangle.append(row)

    return triangle