#!/usr/bin/python3

def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    triangle = []

    # Add the first row with a single element, the number 1
    triangle.append([1])

    # Loop through the remaining rows of the triangle
    for i in range(1, n):
        # Create a new empty row
        row = []
        # The first element of each row is always 1
        row.append(1)
        # Loop through the elements in the previous row and add the sum of the two elements above it to the current row
        for j in range(1, len(triangle[i-1])):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # The last element of each row is also always 1
        row.append(1)
        # Add the current row to the triangle
        triangle.append(row)

    return triangle
