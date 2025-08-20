def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
    # Generate all multiples
    multiples = {}
    result = []

    for i, num in enumerate(candidates):
        if i == 0 or candidates[i-1] != num:
            if num == 0:
                if target == 0:
                    result.append([0])
                    break
                multiples[0] = [[0]]
                continue
                
            m = 1
            while num * m <= target:
                val, multiple = num * m, [num] * m

                if val == target:
                    if multiple not in result:
                        result.append(multiple)
                    break

                cur = multiples.get(val, [])
                if multiple not in cur:
                    cur.append(multiple)
                multiples[val] = cur
                
                m += 1


    # Generate all possible combinations of multiples' values

    nums = list(multiples.keys())
    nums.sort()


    def n_sum(target, n, start):
        if len(nums) - start < n or target < nums[start] * n or target > nums[-1] * n:
            return []
        if n == 2:
            return two_sum(target, start)
        
        res = []
        for i in range(start, len(nums)-n+1):
            if i == start or nums[i] != nums[i-1]:
                for seq in n_sum(target-nums[i], n-1, i+1):
                    res.append([nums[i]] + seq)
        
        return res


    def two_sum(target, start):
        duos = []
        seen = set()

        for i in range(start, len(nums)):
            if len(duos) == 0 or duos[-1][1] != nums[i]:
                if target - nums[i] in seen:
                    duos.append([target - nums[i], nums[i]])
                seen.add(nums[i])
        
        return duos

    
    combinations = []
    for l in range(2, len(nums)+1):
        l_combos = n_sum(target, l, 0)
        if l_combos:
            combinations += l_combos

    
    # Expand the combinations for all possible multiples
    def combinate(combination, c=0):
        if c >= len(combination):
            return []
        
        combinated = []
        for multiple in multiples[combination[c]]:
            seqs = combinate(combination, c+1)
            if seqs:
                for seq in seqs:
                    combinated.append(multiple + seq)
            else:
                combinated.append(multiple)

        return combinated


    expanded_combinations = []
    for combination in combinations:
        expanded_combinations += combinate(combination)


    # Filter out repeated combinations
    filtered_result = []
    for solution in result + expanded_combinations:
        if solution not in filtered_result:
            filtered_result.append(solution)

    return filtered_result
