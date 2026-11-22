class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        nums.sort()
        longestSoFar = 1;
        currentLongest = 1
        currentNum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != currentNum:
                if nums[i]-1 == currentNum:
                    currentLongest += 1
                else:
                    currentLongest = 1
            
            if longestSoFar < currentLongest:
                longestSoFar = currentLongest

            currentNum = nums[i]
        return longestSoFar
            