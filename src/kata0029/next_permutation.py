def next_permutation(self, nums: list[int]) -> None:
    i = j = len(nums) - 1

    while nums[i] <= nums[i-1] and i > 0:
        i -= 1
    
    pivot = i - 1

    if pivot < 0:
        nums.reverse()
        return

    while nums[j] <= nums[pivot]:
        j -= 1
    
    next_num = nums[j]
    nums[j] = nums[pivot]
    nums[pivot] = next_num

    nums[i:] = nums[len(nums)-1:i-1:-1]
