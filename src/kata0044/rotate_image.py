def rotate_image(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for i in range(n//2):
        for j in range(n-n//2):
            matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                        matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]
