class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mymap = defaultdict(int)

        for num in nums:
            mymap[num] += 1

        mybucket = [[] for i in range(len(nums)+1)]
        
        for num, freq in mymap.items():
            mybucket[freq].append(num)
        
        res = []
        for i in range(len(mybucket)-1,0,-1):
            res.extend(mybucket[i])
            if len(res)==k:
                return res
        return res
