def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    trios = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        if nums[i] > 0:
            break

        left, right = i + 1, len(nums) - 1

        while left < right:
            sum_trio = nums[i] + nums[left] + nums[right]
            if sum_trio == 0:
                trios.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif sum_trio > 0:
                right -= 1

            else:
                left += 1

    return trios