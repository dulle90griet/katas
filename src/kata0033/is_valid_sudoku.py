def is_valid_sudoku(board: list[list[str]]) -> bool:
    nums = "123456789"

    # iterate over rows (O(n))
    for row in board:
        count = {}
        for tile in row:
            if tile in nums:
                count[tile] = count.get(tile, 0) + 1
                if count[tile] > 1:
                    return False
        
    # iterate over columns (O(n))
    for col in range(len(board[0])):
        count = {}
        for row in board:
            tile = row[col]
            if tile in nums:
                count[tile] = count.get(tile, 0) + 1
                if count[tile] > 1:
                    return False

    # iterate over squares
    def get_coords(n):
        return n % 3, n // 3

    for square in range(9):
        count = {}
        x, y = get_coords(square)
        start_row = y * 3
        start_col = x * 3

        for subsquare in range(9):
            x, y = get_coords(subsquare)
            row = start_row + y
            col = start_col + x

            tile = board[row][col]
            if tile in nums:
                count[tile] = count.get(tile, 0) + 1
                if count[tile] > 1:
                    return False
    
    return True
