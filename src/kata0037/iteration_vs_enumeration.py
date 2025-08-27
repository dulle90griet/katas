""" Use a decorator to compare the process times in Python of basic index iteration and enumeration.
"""

import time
import sys


def time_func(func):
    def arg_handler(*args, **kwargs):
        start = time.process_time()
        func(*args, **kwargs)
        end = time.process_time()
        return end - start

    return arg_handler


@time_func
def range_iterator(nums: list[int]) -> None:
    for i in range(len(nums)):
        res = f"{i}: {nums[i]}"


@time_func
def foreach_iterator(nums: list[int]) -> None:
    i = 0
    for num in nums:
        res = f"{i}: {num}"
        i += 1


@time_func
def enumerator(nums: list[int]) -> None:
    for i, x in enumerate(nums):
        res = f"{i}: {x}"


scale = 10**6
nums = list(range(scale))
reps = int(sys.argv[1])

print(f"Iterating over {scale} numbers...\n")

print("SINGLE REP\n==========")
rep_times = {
    "range": range_iterator(nums),
    "foreach": foreach_iterator(nums),
    "enum": enumerator(nums)
}
sorted_times = sorted(list(rep_times.keys()), key=lambda x: rep_times[x])
for i, key in enumerate(sorted_times):
    print(f" {i+1}. {key} ({rep_times[key]:0.6f}s)")

print(f"\n{reps}-REP AVG\n"+"="*(8+len(str(reps))))
rep_times = {
    "range": sum([range_iterator(nums) for _ in range(reps)]) / reps,
    "foreach": sum([foreach_iterator(nums) for _ in range(reps)]) / reps,
    "enum": sum([enumerator(nums) for _ in range(reps)]) / reps
}
sorted_times = sorted(list(rep_times.keys()), key=lambda x: rep_times[x])
for i, key in enumerate(sorted_times):
    print(f" {i+1}. {key} ({rep_times[key]:0.6f}s)")

