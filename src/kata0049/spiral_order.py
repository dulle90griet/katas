def spiral_order(matrix: list[list[int]]) -> list[int]:
    m, n = len(matrix[0]), len(matrix)
    pos = [0, 0]
    vector = [1, 0]
    spiral = []
    visited = set()

    for _ in range(m*n):
        spiral.append(matrix[pos[1]][pos[0]])
        visited.add(tuple(pos))

        next_pos = [pos[0] + vector[0], pos[1] + vector[1]]
        if (tuple(next_pos) in visited
            or 0 > next_pos[0] or next_pos[0] >= m
            or 0 > next_pos[1] or next_pos[1] >= n):
            vector = [-vector[1], vector[0]]

        pos[0] += vector[0]
        pos[1] += vector[1]
    
    return spiral
