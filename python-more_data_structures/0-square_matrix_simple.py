#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    CREATE empty list matrix new_matrix

    FOR each row IN matrix:
        CREATE empty list new_row

        FOR each value IN row:
            square = value * value
            ADD square TO new_row

        ADD new_row TO new_matrix
    
    RETURN new_matrix

    """
    return [[value ** 2 for value in row] for row in matrix]

