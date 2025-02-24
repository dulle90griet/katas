""" Given an integer array, `height`, and imagining its elements graphed such that each `ith` element forms a line from `(i, 0)` to `(i, height[i])`, find the two lines that together with the x-axis form the container capable of storing the greatest quantity (2D) water. Return the quantity (area) of water stored. """

def max_fluid_area(height: list[int]) -> int:
    n = len(height)

    height_map = {height[0]: [None, 0, None]}
    if height[n-1] in height_map:
        height_map[height[n-1]][2] = n-1
    else:
        height_map[height[n-1]] = [None, None, n-1]
    left_logged = 0
    right_logged = n-1

    i = 1
    while i < n:
        left = i
        right = n - i - 1

        if left < right_logged:
            if height[left] > height[left_logged]:
                if height[left] in height_map:
                    height_map[height[left]][1] = left
                else:
                    height_map[height[left]] = [None, left, None]
                left_logged = left
        if right > left_logged:
            if height[right] > height[right_logged]:
                if height[right] in height_map:
                    height_map[height[right]][2] = right
                else:
                    height_map[height[right]] = [None, None, right]
                right_logged = right
        else:
            break
        
        i += 1
    
    sorted_keys = sorted(height_map.keys())
    for i in range(len(sorted_keys)):
        height_map[sorted_keys[i]][0] = i

    max_area = 0
    for cur_height in sorted_keys:
        left = height_map[cur_height][1]
        right = height_map[cur_height][2]

        if (height_map[cur_height][0] == len(sorted_keys) - 1
            and (left is None or right is None)):
            continue
        if left is None:
            for i in range(height_map[cur_height][0] + 1, len(sorted_keys)):
                next_left = height_map[sorted_keys[i]][1]
                if next_left is not None:
                    left = next_left
                    break
                else:
                    next_right = height_map[sorted_keys[i]][2]
                    if next_right is not None and next_right < right:
                        left = next_right
            if left is None: break
        elif right is None:
            for i in range(height_map[cur_height][0] + 1, len(sorted_keys)):
                next_right = height_map[sorted_keys[i]][2]
                if next_right is not None:
                    right = next_right
                    break
                else:
                    next_left = height_map[sorted_keys[i]][1]
                    if next_left is not None and next_left > left:
                        right = next_left
            if right is None: break

        area = cur_height * (right - left)
        max_area = max(area, max_area)

    return max_area