def combination_sum_2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    res, path = [], []
    def dfs(idx, cur):
        if cur == target:
            res.append(path[:])
            return
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            if cur + candidates[i] > target:
                break
            path.append(candidates[i])
            dfs(i+1, cur+candidates[i])
            path.pop()
        
    dfs(0, 0)
    return res
