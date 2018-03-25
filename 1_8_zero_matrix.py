def zero_matrix(matrix):

    zero_rows = set()
    zero_cols = set()
    for row_idx in xrange(len(matrix)):
        for col_idx in xrange(len(matrix[row_idx])):
            if matrix[row_idx][col_idx] == 0:
                zero_rows.add(row_idx)
                zero_cols.add(col_idx)

    print zero_rows

    new_matrix = []
    for row_idx in xrange(len(matrix)):
        new_matrix.append([])
        for col_idx in xrange(len(matrix[row_idx])):
            if(row_idx in zero_rows or col_idx in zero_cols):
                new_matrix[row_idx].append(0)
            else:
                new_matrix[row_idx].append(matrix[row_idx][col_idx])
    return new_matrix
