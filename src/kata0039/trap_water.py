def trap_water(height: list[int]) -> int:
    trapped, basin, left = 0, 0, 0

    for right in range(1, len(height)):
        if height[right] == 0:
            continue

        if height[right] >= height[left]:
            width = right - (left + 1)
            trapped += width * min(height[left], height[right]) - basin
            left = right
            basin = 0
        else:
            basin += height[right]

    if left == len(height) - 1:
        return trapped

    last_left = left
    basin, right = 0, len(height)-1

    for left in range(len(height)-2, last_left-1, -1):
        if height[left] == 0:
            continue

        if height[left] >= height[right]:
            width = right - (left + 1)
            trapped += width * min(height[left], height[right]) - basin
            right = left
            basin = 0
        elif right != left:
            basin += height[left]

    return trapped
