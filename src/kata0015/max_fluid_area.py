""" Given an integer array, `height`, and imagining its elements graphed such that each `ith` element forms a line from `(i, 0)` to `(i, height[i])`, find the two lines that together with the x-axis form the container capable of storing the greatest quantity (2D) water. Return the quantity (area) of water stored. """

def max_fluid_area(height: list[int]) -> int:
    n = len(height)

    max_area = 0

    for i in range(n):
        for j in range(i+1, n):
            area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, area)
    
    return max_area