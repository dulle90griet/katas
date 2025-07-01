class Solution:
    # first attempt
    def containsDuplicate(self, nums: List[int]) -> bool:
        discovered = {}
        for num in nums:
            if num in discovered:
                return True
            discovered[num] = None
        return False
        ```

	# more efficient
	def containsDuplicate(self, nums: List\[int]) -> bool:
        return len(set(nums)) != len(nums)