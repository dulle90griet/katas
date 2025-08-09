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

    # find the leftmost matching number
    if found > 0:
        l, r = 0, found - 1
        if nums[r] == target:
            while l < r:
                m = (l + r) // 2

                if nums[m] < target:
                    l = m + 1
                else:
                    r = m    
                
            left_bound = l

    # find the rightmost matching number
    if found == len(nums) - 2:
        if nums[found+1] == target:
            right_bound = found+1
    elif found < len(nums) - 2:
        l, r = found + 1, len(nums) - 1

        if nums[l] == target:
            while r > l:
                if nums[l] == nums[r]:
                    l = r
                    break

                if r - l == 1 and nums[l] != nums[r]:
                    r = l

                m = (l + r) // 2

                if nums[m] > target:
                    r = m - 1
                else:
                    l = m
        
            right_bound = l

    return left_bound, right_bound
