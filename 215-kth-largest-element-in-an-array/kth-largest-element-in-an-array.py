import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.k=k
        self.heap=nums
        heapq.heapify(self.heap)
        while len(self.heap)>self.k:
            heapq.heappop(self.heap)
        return self.heap[0]    

        