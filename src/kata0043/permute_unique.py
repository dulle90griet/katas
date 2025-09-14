def permute_unique(nums: list[int]) -> list[list[int]]:
    nums.sort()

    def backtrack(nums: list[int], path: list[int], ans: list[list[int]]) -> None:
        if not nums:
            ans.append(path[:])
        
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            
            hold, nums[:] = n, nums[:i]+nums[i+1:]
            path.append(n)
            backtrack(nums, path, ans)
            path.pop()
            nums[:] = nums[:i]+[hold]+nums[i:]
    
    ans = []
    backtrack(nums, [], ans)
    return ans
