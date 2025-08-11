def is_valid_sudoku(board: list[list[str]]) -> bool:
    row_map = [set() for _ in range(9)]
    col_map = [set() for _ in range(9)]
    box_map = [set() for _ in range(9)]

    for y in range(len(board)):
        for x in range(len(board[0])):
            tile = board[y][x]
            n = 3*(y//3)+(x//3)

            if tile != ".":
                if tile in row_map[y] or tile in col_map[x] or tile in box_map[n]:
                    return False
                
                row_map[y].add(tile)
                col_map[x].add(tile)
                box_map[n].add(tile)
        
    return True
