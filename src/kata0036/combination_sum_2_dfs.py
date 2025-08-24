def combination_sum_2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    res = []
    def dfs(idx, path, cur):
        if cur == target:
            res.append(path)
            return
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            if cur + candidates[i] > target:
                break
            dfs(i+1, path+[candidates[i]], cur+candidates[i])
        return
    dfs(0, [], 0)
    return res
