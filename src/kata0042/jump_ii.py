def jump_2(nums: list[int]) -> int:
    def dfs(nums, start, limit, ans, path):
        if start == len(nums) - 1:
            if ans == []:
                ans.append(path[:])
            elif len(path) < len(ans[-1]):
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

    ans = []   
    dfs(nums, 0, nums[0], ans, [])

    return len(ans[-1])