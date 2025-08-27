""" Use a decorator to compare the process times in Python of basic index iteration and enumeration.
"""

import time

def time_func(func):
    def arg_handler(*args, **kwargs):
        start = time.process_time()
        func(*args, **kwargs)
        end = time.process_time()
        return end - start

    return arg_handler

@time_func
def iterator(nums: list[int]) -> None:
    for i in range(len(nums)):
        idx = i
        num = nums[i]

@time_func
def enumerator(nums: list[int]) -> None:
    for i, x in enumerate(nums):
        idx = i
        num = x


nums = list(range(10**6))

print(iterator(nums))
print(enumerator(nums))

