""" Given an integer array, `height`, and imagining its elements graphed such that each `ith` element forms a line from `(i, 0)` to `(i, height[i])`, find the two lines that together with the x-axis form the container capable of storing the greatest quantity (2D) water. Return the quantity (area) of water stored. """

def max_fluid_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0
    max_height = max(height)

    while left < right:
        width = right - left

        if height[left] < height[right]:
            max_area = max(max_area, width * height[left])
            left += 1
        else:
            max_area = max(max_area, width * height[right])
            right -= 1
            
        if width * max_height < max_area:
            return max_area

    return max_area