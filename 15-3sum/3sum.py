class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        re=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            le,ri=i+1,len(nums)-1
            while le<ri:
                tot=nums[i]+nums[le]+nums[ri]
                if tot<0:
                    le+=1
                elif tot>0:
                    ri-=1
                else:
                    re.append([nums[i],nums[le],nums[ri]]) 
                    while le<ri and nums[le]==nums[le+1] :
                        le+=1 
                    while le<ri and nums[ri]==nums[ri-1] :
                        ri-=1  
                    le+=1
                    ri-=1
        return re                        

        