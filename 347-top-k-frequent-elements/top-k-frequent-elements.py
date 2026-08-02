import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        heap=[]
        for num,count in freq.items():
            heapq.heappush(heap,(count,num))
            if len(heap)>k:
                heapq.heappop(heap)


        ans=[] 
        while heap:
            count,num=heapq.heappop(heap)
            ans.append(num)
        return ans            

        