def get_sub_square(matrix, x_offset, y_offset):
    sub_square = []
    for y in range(y_offset, y_offset + 3):
        sub_row = []
        for x in range(x_offset, x_offset + 3):
            sub_row.append(matrix[y][x])
        sub_square.append(sub_row)
    
    return sub_square