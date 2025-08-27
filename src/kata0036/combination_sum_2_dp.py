def combination_sum_2(candidates: list[int], target: int) -> list[list[int]]:
    dp = [[] for _ in range(target+1)]
    dp[0] = [[]]
    seen = set()
    candidates.sort()

    for c in candidates:
        c_dp = [[] for _ in range(target+1)]

        for t in range(c, target+1):
            if t - c == 0:
                if c in seen:
                    continue
                seen.add(c)
            
            for combo in dp[t-c]:
                new = combo + [c]
                if new not in dp[t]:
                    c_dp[t].append(new)

        for i, c_grp in enumerate(c_dp):
            if c_grp:
                dp[i] += c_grp
    
    return dp[target]
