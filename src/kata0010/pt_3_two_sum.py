def two_sum(nums: list[int], target: int) -> list[int]:
    # # brute-force approach - O(n^2)
    # n = len(nums)
    # for i in range(n-1):
    #     for j in range(i+1, n):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    # hash table approach - O(n)
    num_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in num_map:
            return [num_map[complement], i]
        num_map[nums[i]] = i