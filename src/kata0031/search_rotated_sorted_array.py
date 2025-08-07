def search_rotated_sorted_array(nums: list[int], target: int) -> int:
    pivot = 0

    if nums[-1] < nums[0]:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] >= nums[0]:
                left = middle + 1
            else:
                right = middle
        
        pivot = left

        nums = nums[pivot:] + nums[:pivot]

    left, right = 0, len(nums) - 1
    
    while left <= right:
        middle = (left + right) // 2

        if nums[middle] == target:
            return (middle + pivot) % len(nums)
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1