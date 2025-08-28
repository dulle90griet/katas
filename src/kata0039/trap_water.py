def trap_water(height: list[int]) -> int:
    trapped = max_left = max_right = 0
    left, right = 0, len(height) - 1

    while left < right:
        if height[left] <= height[right]:
            if height[left] > max_left:
                max_left = height[left]
            else:
                trapped += max_left - height[left]
            left += 1
        else:
            if height[right] > max_right:
                max_right = height[right]
            else:
                trapped += max_right - height[right]
            right -= 1
    
    return trapped
