def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
    sums = {}
    result = []

    for c in candidates:
        i = 1
        while c * i <= target:
            s = c * i
            l = [c] * i
            if s == target:
                if l not in result:
                    result.append(l)
            else:
                complement = target - s
                if complement in sums:
                    for combo in sums[complement]:
                        if combo + l not in result:
                            result.append(combo + l)
                if s in sums:
                    if l not in sums[s]:
                        sums[s].append(l)
                else:
                    sums[s] = [l]
            i += 1

    return result