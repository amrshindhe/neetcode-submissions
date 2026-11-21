class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # O(n log n)

        if len(nums) <= 1:
            return False

        for inx, value in enumerate(nums):
            if value == nums[inx - 1]:
                return True

        return False