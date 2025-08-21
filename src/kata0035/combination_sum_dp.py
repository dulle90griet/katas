def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    dp = [[] for n in range(target + 1)]
    dp[0] = [[]]

    for c in candidates:
        for t in range(c, target+1):
            if t - c == 0 or dp[t-c]:
                for combo in dp[t-c]:
                    dp[t].append(combo + [c])
    
    return dp[target]
