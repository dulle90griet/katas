def trap_water(height: list[int]) -> int:
    trapped = 0
    left, right = 0, len(height) - 1
    prev_lowest = 0

    while left < right:
        cur_lowest = min(height[left], height[right])
        if cur_lowest > prev_lowest:
            height_diff = cur_lowest - prev_lowest
            width = right - (left + 1)
            trapped += width * height_diff
            prev_lowest = cur_lowest

        if height[right] >= height[left]:
            left += 1
            if trapped > 0 and right > left:
                trapped -= min(height[left], prev_lowest)
        else:
            right -= 1
            if trapped > 0 and right > left:
                trapped -= min(height[right], prev_lowest)
    
    return trapped
