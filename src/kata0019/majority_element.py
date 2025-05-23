def majority_element(nums: list[int]) -> int:
    # Define a tracking variable, where index 0 is the number to track
    # and index 1 is the count
    t = [None, 0]

    for num in nums:
        if t[1] == 0:
            # If the count is 0, we've either just started checking
            # or the previously tracked num has been outnumbered
            t[0] = num
            t[1] = 1
        elif t[0] == num:
            # num is tracked number: increment count
            t[1] += 1
        else:
            # For each non-tracked number encountered, decrement the count
            t[1] -= 1

    # We're told to assume a majority element exists in the array,
    # so can simply return the surviving (highest-incidence) tracked number
    return t[0]
