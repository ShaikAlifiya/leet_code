class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        p=0
        mp={0:1}
        c=0

        for i in nums:
            if i%2 ==1:
                p+=1

            if p-k in mp:
                c=c+mp[p-k]
            mp[p]=mp.get(p,0)+1
        return c            
        