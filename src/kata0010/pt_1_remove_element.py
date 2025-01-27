def remove_element(nums: list[int], val: int) -> None:
    # # first attempt - approaches O(n^2) complexity
    # for i in range(len(nums)-1, -1, -1):
    #     if nums[i] == val:
    #         nums.pop(i)
    # return len(nums)

    # second attempt - O(n) complexity
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j

    # # another, extremely Pythonic solution
    # nums[:] = [i for i in nums if i != val]
    # return len(nums)