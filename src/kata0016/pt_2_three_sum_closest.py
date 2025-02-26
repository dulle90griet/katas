def three_sum_closest(nums: list[int], target: int) -> int:
    min_diff = float('inf')
    ans = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            trio = [nums[i], nums[left], nums[right]]
            sum_trio = sum(trio)

            if sum_trio == target:
                return sum_trio
            
            diff = abs(sum_trio - target)
            if diff < min_diff:
                min_diff = diff
                ans = sum_trio
            
            if sum_trio < target:
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                left +=1
            else:
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                right -= 1
    
    return ans