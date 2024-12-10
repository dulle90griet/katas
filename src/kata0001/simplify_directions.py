def simplify_directions(list_of_directions):
    direction_values = {
        "NORTH": [0, 1],
        "SOUTH": [0, -1],
        "EAST": [1, 0],
        "WEST": [-1, 0],
    }

    movement = [0, 0]

    for direction in list_of_directions:
        movement[0] += direction_values[direction][0]
        movement[1] += direction_values[direction][1]

    simplified_directions = []

    if movement[1] > 0:
        simplified_directions += ["NORTH"] * movement[1]
    elif movement[1] < 0:
        simplified_directions += ["SOUTH"] * (-1 * movement[1])

    if movement[0] > 0:
        simplified_directions += ["EAST"] * movement[0]
    elif movement[0] < 0:
        simplified_directions += ["WEST"] * (-1 * movement[0])

    return simplified_directions
