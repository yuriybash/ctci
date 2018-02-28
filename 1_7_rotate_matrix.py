def rotate_matrix(matrix):
    size = len(matrix)
    new = [[None for x in range(size)] for i in range(size)]
    for row in xrange(size):
        for col in xrange(size):
            new[col][size-row-1] = matrix[row][col]
    return new
