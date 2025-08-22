def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]

    for c in candidates:
        for t in range(c, target+1):
            if dp[t-c]:
                for combo in dp[t-c]:
                    dp[t].append(combo + [c])
    
    return dp[target]
