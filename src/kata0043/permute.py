def permute(nums: list[int]) -> list[list[int]]:
    def backtrack(
        nums: list[int], 
        used: set[int], 
        ans: list[list[int]], 
        path: list[int]
    ) -> None:
        if len(path) == len(nums):
            ans.append(path[:])
            return
        
        for i, n in enumerate(nums):
            if i not in used:
                used |= {i}
                path.append(n)
                backtrack(nums, used, ans, path)
                path.pop()
                used -= {i}
    
    ans = []
    backtrack(nums, set(), ans, [])
    return ans
