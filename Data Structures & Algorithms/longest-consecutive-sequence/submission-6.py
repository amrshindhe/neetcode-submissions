class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<=1:
            return len(nums)

        highestStreak = 1
        currentHighest = nums[0]
        currentStreak = 1

        indx = 1
        while indx < len(nums):
            if nums[indx]-1 == currentHighest:
                currentStreak += 1
            elif nums[indx] == currentHighest:
                pass
            else:
                currentStreak = 1

            if currentStreak > highestStreak:
                highestStreak = currentStreak
            currentHighest = nums[indx]
            indx += 1
        return highestStreak