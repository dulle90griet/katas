def contains_duplicate(nums: list[int]) -> bool:
    discovered = {}
    for num in nums:
        if num in discovered:
            return True
        discovered[num] = None
    return False