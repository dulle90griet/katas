def trap_water(height: list[int]) -> int:
    trapped = 0

    n = 1
    while True:
        row_tiles = 0
        is_wall = False
        is_basin = False
        last_wall = 0

        for i, h in enumerate(height):
            if h >= n:
                if is_basin:
                    trapped += i - last_wall - 1
                    is_basin = False
                is_wall = True
                last_wall = i
                row_tiles += 1
            else:
                if is_wall:
                    is_basin = True
                is_wall = False
        
        if row_tiles <= 1:
            break
        
        n += 1
    
    return trapped