def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans, cur_combo = [], []

        def combination(cur_sum, cur_idx):
            if cur_sum > target:
                return
            if cur_sum == target:
                ans.append([el for el in cur_combo])

            for i in range(cur_idx, len(candidates)):
                cur_combo.append(candidates[i])
                combination(cur_sum + candidates[i], i)
                cur_combo.pop()

        combination(0, 0)

        return ans
