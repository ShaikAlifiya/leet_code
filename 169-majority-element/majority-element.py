class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        mp={}
        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]]+=1
            else:
                mp[nums[i]]=1
        for key,values in mp.items():
            if values==max(mp.values()):
                return key            
        