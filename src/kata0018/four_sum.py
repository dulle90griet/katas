def four_sum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()


    def n_sum(target :int, n :int, start :int) -> list[list[int]]:
        if (len(nums) - start < n
                or target < nums[start] * n
                or target > nums[-1] * n):
            return []
        if n == 2:
            return two_sum(target, start)
        
        res = []
        for i in range(start, len(nums) - n + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue
            
            for seq in n_sum(target - nums[i], n - 1, i + 1):
                res.append([nums[i]] + seq)
        
        return res


    def two_sum(target :int, start :int) -> list[list[int]]:
        duos = []
        seen = set()

        for i in range(start, len(nums)):
            if len(duos) == 0 or duos[-1][1] != nums[i]:
                if target - nums[i] in seen:
                    duos.append([target - nums[i], nums[i]])
            seen.add(nums[i])

        return duos
    

    return n_sum(target, 4, 0)
