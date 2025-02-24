def three_sum(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    if n < 3:
        return []
    elif n == 3 and sum(nums) == 0:
        return [nums]

    checked = set()
    sorted_nums = sorted(nums)
    trios = []

    def two_sum(target :int, ignore :int) -> list[int]:
        num_map = {}
        solutions = []
        for j in range(ignore + 1, len(sorted_nums)):
            if sorted_nums[j] not in checked:
                complement = target - sorted_nums[j]
                if complement in num_map:
                    solution = [complement, sorted_nums[j]]
                    if solution not in solutions:
                        solutions.append(solution)
                num_map[sorted_nums[j]] = j
        return solutions

    for i in range(n):
        target = 0 - sorted_nums[i]
        if target not in checked and sorted_nums[i] not in checked: 
            trios += [[sorted_nums[i], x, y] for x, y in two_sum(target, i)]
        checked.add(sorted_nums[i])
    
    return sorted(sorted(x) for x in trios)