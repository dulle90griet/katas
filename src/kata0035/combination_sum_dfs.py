def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    ans, path = [], []

    def combination(start, total):
        if total > target:
            return
        if total == target:
            ans.append(path[:])
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            combination(i, total + candidates[i])
            path.pop()

    combination(0, 0)

    return ans
