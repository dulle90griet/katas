def find_first_and_last(nums: list[int], target: int) -> tuple[int]:
    found = -1
    l, r = 0, len(nums) - 1

    # find a position containing the target number
    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            found = m
            break
        if nums[m] > target:
            r = m - 1
        else:
            l = m + 1

    if found == -1:
        return -1, -1

    left_bound = right_bound = found

    if found > 0:
        # find the leftmost matching number
        l, r = 0, found - 1
        if nums[r] < target:
            left_bound = r + 1
        else:
            while l < r:
                m = (l + r) // 2

                if nums[m] < target:
                    l = m + 1
                else:
                    r = m    
                
            left_bound = l

    if found < len(nums) - 1:
        # find the rightmost matching number
        l, r = found + 1, len(nums) - 1
        if nums[l] > target:
            right_bound = l - 1
        else:
            while r > l:
                m = (l + r) // 2

            if nums[m] > target:
                r = m -1
            else:
                l = m
        
            right_bound = r

    return left_bound, right_bound
