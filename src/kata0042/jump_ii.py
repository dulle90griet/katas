def jump_2(self, nums: List[int]) -> int:
    ans = []

    def dfs(nums, start, limit, ans, path):
        if start == len(nums) - 1:
            if ans and path and len(path) < len(ans):
                ans.pop()
                ans.append(path[:])
                return
        elif start >= len(nums):
            return
        
        limit = min(len(nums) - 1 - start, limit)
        for i in range(start+1, start+limit+1):
            path.append(i)
            dfs(nums, i, nums[i], ans, path)
            path.pop()
    
    dfs(nums, 0, nums[0], ans, [])

    return dfs