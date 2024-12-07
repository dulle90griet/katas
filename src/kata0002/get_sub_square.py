def get_sub_square(matrix, x_offset, y_offset):
    sub_square = []
    for y in range(0, 3):
        sub_row = []
        for x in range(0, 3):
            sub_row.append(matrix[y][x])
        sub_square.append(sub_row)
    
    return sub_square