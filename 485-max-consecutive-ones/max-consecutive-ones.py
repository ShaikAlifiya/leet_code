class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter=0
        ms=0
        for i in range(len(nums)):
            if nums[i]==1:
                counter+=1
                ms=max(counter,ms)
            
            
            else:
                
                counter=0
        return ms            

            
                   


           
                
                  
        