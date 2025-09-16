def rotate_image(matrix: list[list[int]]) -> None:
    c = len(matrix[0]) // 2
    c_width = 1 if len(matrix[0]) % 2 else 0

    for layer in range(1, c + 1):
        layer_size = 2 * layer + c_width

        for pixel in range(layer_size - 1):
            x_offset, y_offset = pixel - layer, -layer

            last = matrix[c + y_offset][c + x_offset]

            for side in range(4):
                # 90 degree CW transformation of 2D vector when y-axis
                # increases downwards is (x, y) -> (-y, x)
                x_offset, y_offset = -y_offset, x_offset

                swap_x, swap_y = c + x_offset, c + y_offset

                if not c_width:
                    match side:
                        case 0:
                            swap_x -= 1
                        case 1:
                            swap_x -= 1
                            swap_y -= 1
                        case 2:
                            swap_y -= 1

                last, matrix[swap_y][swap_x] = matrix[swap_y][swap_x], last
