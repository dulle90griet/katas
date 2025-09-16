def rotate_image(matrix: list[list[int]]) -> None:
    m = {(0, 1): "r", (1, 0): "d", (0, -1): "l", (-1, 0): "u"}

    c = len(matrix[0]) // 2
    rdiff = 0 if len(matrix[0]) % 2 else -1

    for i in range(1, c + 1):
        mov = (0, 1) # Start moving right
        x = y = c - i

        for shift in range(2 * i + rdiff):
            last = matrix[c-i][c-i]

            while True:
                if (m[mov] == "r" and x == c + i + rdiff) or (m[mov] == "d" and y == c + i + rdiff) or (m[mov] == "l" and x == c - i):
                    # 90 degree CW transformation of 2D vector when y-axis increases downwards
                    # is (y, x) -> (x, -y)
                    mov = (mov[1], -mov[0])
                elif m[mov] == "u" and y == c - i:
                    # one shift circuit completed
                    mov = (mov[1], -mov[0])
                    break
                
                x += mov[1]
                y += mov[0]

                last, matrix[y][x] = matrix[y][x], last
