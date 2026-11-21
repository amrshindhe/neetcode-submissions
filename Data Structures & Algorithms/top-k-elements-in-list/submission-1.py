class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = defaultdict(int)

        for num in nums:
            mydict[num] += 1
        
        myheap = []

        for num, freq in mydict.items():
            heapq.heappush(myheap, (-freq,num))
        res = []
        for i in range(k):
            a , num = heapq.heappop(myheap)
            res.append(num)
        
        return res