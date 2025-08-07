def search_rotated_sorted_array(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] == target:
            return middle

        if (target >= nums[0]) == (nums[middle] >= nums[0]):
            num = nums[middle]
        else:
            num = float('-inf') if nums[middle] >= nums[0] else float('inf') 

        if num < target:
            left = middle + 1
        else:
            right = middle - 1
    
    return -1
