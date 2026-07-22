class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w_sum=sum(nums[:k])
        m_sum=w_sum
        for i in range(k,len(nums)):
            w_sum+=nums[i]
            w_sum-=nums[i-k]
            m_sum=max(m_sum,w_sum)
        return m_sum/k   
        