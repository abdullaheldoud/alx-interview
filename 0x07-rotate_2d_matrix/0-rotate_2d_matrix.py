def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - 1 - layer
        for i in range(first, last):
            # Save the top element
            top = matrix[first][i]

            # Move left to top
            matrix[first][i] = matrix[last - (i - first)][first]

            # Move bottom to left
            matrix[last - (i - first)][first] = matrix[last][last - (i - first)]

            # Move right to bottom
            matrix[last][last - (i - first)] = matrix[i][last]

            # Move top to right
            matrix[i][last] = top

# Testing the function
if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    for row in matrix:
        print(row)

