class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx,value in enumerate(nums):
            j = idx+1
            while j<len(nums):
                if value + nums[j] == target:
                    return [idx, j]
                j += 1
        