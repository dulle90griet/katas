from copy import deepcopy

def fill_square(input_list):
    """
    Fills a list out to a square matrix.

    Given a list of dimensions <= 2, returns a square matrix with None in all previously empty positions.

    Args:
        input_list:
            The list to be filled out.

    Returns:
        A list constituting a square matrix.
    
    """
    
    working_list = deepcopy(input_list)

    if not working_list:
        return []
    
    y_length = len(working_list)
    max_x_length = 0

    for y in range(y_length):
        if type(working_list[y]) != list:
            working_list[y] = [working_list[y]]
        
        max_x_length = max(max_x_length, len(working_list[y]))

    longest_side = max(y_length, max_x_length)

    for _ in range(longest_side - y_length):
        working_list.append([])

    for y in range(longest_side):
        for _ in range(longest_side - len(working_list[y])):
            working_list[y].append(None)
    
    return working_list