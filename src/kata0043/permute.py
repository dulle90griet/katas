def permute(nums: list[int]) -> list[list[int]]:
    def backtrack(nums: list[int], start: int, ans: list[list[int]]) -> None:
        if start >= len(nums):
            ans.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            nums[i], nums[start] = nums[start], nums[i]
            backtrack(nums, start+1, ans)
            nums[i], nums[start] = nums[start], nums[i]
    
    ans = []
    backtrack(nums, 0, ans)
    return ans
