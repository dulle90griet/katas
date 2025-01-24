def remove_element(nums: list[int], val: int) -> None:
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == val:
            nums.pop(i)
    
    return len(nums)