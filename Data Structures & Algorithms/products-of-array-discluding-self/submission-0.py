class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preCounter = 1
        preList = defaultdict(int)

        for i, num in enumerate(nums):
            preCounter *= num
            preList[i] = preCounter

        postCounter = 1
        postList = defaultdict(int)

        for i in range(len(nums)-1,0,-1):
            postCounter *= nums[i]
            postList[i] = postCounter
        
        res = [0] * len(nums)

        res[0] = postList[1]
        res[len(nums)-1] = preList[len(nums)-2]
        for i in range(1,len(nums)-1):
            res[i] = preList[i-1]*postList[i+1]
        
        return res
