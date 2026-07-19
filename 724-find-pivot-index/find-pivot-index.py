class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lef=[]
        for i in range(len(nums)):
            s= sum(lef)
            t=sum(nums[i+1:len(nums)])
            if s==t:
                return i
            else:
                lef.append(nums[i])   
        return -1         
        