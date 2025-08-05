def next_permutation(self, nums: list[int]) -> None:
    if len(nums) < 2:
        return True

    i = len(nums) - 1

    while nums[i] <= nums[i-1] and i > 0:
        i -= 1
    
    pivot = i - 1

    if pivot < 0:
        nums.reverse()
        return True

    next_num = min([num for num in nums[i:] if num > nums[pivot]], key=lambda x: x - nums[pivot])
    for j in range(len(nums)-1, pivot, -1):
        if nums[j] == next_num:
            swap = j
            break
    
    nums[swap] = nums[pivot]
    nums[pivot] = next_num

    nums[i:] = reversed(nums[i:])
    