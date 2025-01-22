"""
Given two integer lists sorted in ascending order, `nums1` and `nums2`, and two integers, `m` and `n`, representing the number of elements to be used from the beginnings of `nums1` and `nums2` respectively, merge the two lists into a single list sorted in ascending order. `nums1` is assumed to have a length of m + n, and the final sorted list should be produced by modifying `nums1` in place, not by returning a new list.
"""

def merge(nums1, m, nums2, n):
    cur1 = m-1
    cur2 = n-1

    for cur3 in range(m+n-1, -1, -1):
        if cur2 < 0:
            break

        if cur1 >= 0:
            if nums1[cur1] > nums2[cur2]:
                nums1[cur3] = nums1[cur1]
                cur1 -= 1
                continue
        
        nums1[cur3] = nums2[cur2]
        cur2 -= 1