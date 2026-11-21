class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for idx, value in enumerate(nums):
            complement = target - value
            if complement in myDict:
                return [myDict[complement],idx]
            myDict[value] = idx
        return []
        