""" Given an integer array, `nums`, find the subarray with the largest sum, and return its sum. """

def max_sub_array(nums: list[int]) -> int:
    max = nums[0]
    cur = 0
    for i in range(1, len(nums)):
        cur += nums[i]
        if cur > max:
            max = cur
        elif cur < 0:
            cur = 0
    return max