def four_sum(nums: list[int], target: int) -> list[list[int]]:
    quads = []
    nums.sort()

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0 and nums[i] > target:
            break

        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            if nums[j] > 0 and nums[i] + nums[j] > target:
                break

            left, right = j + 1, len(nums) - 1

            while left < right:
                quad = [nums[i], nums[j], nums[left], nums[right]]
                sum_quad = sum(quad)

                if sum_quad == target:
                    quads.append(quad)

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif sum_quad < target:
                    left += 1
                else:
                    right -= 1
    
    return quads