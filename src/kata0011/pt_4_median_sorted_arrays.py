""" Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`. """


# Solution with O(log (m + n)) complexity
def find_median_of_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
    i = j = 0
    merged = []

    if len(nums2) > len(nums1):
        nums1, nums2 = nums2, nums1
    
    while i < len(nums1):
        if j < len(nums2) and nums2[j] < nums1[i]:
            merged.append(nums2[j])
            j += 1
        else:
            merged.append(nums1[i])
            i += 1
    
    if j < len(nums2):
        merged += nums2[j:]

    midpoint = len(merged) // 2
    if len(merged) % 2 == 1:
        return merged[midpoint]
    else:
        return (merged[midpoint-1] + merged[midpoint]) / 2