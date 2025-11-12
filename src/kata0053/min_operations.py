def min_operations(nums: list[int]) -> int:
    stack = []
    ans = 0

    for num in nums:
        while len(stack) > 0 and num < stack[-1]:
            stack.pop()
        
        if len(stack) == 0 or num > stack[-1]:
            if num == 0:
                continue

            stack.append(num)
            ans += 1
    
    return ans