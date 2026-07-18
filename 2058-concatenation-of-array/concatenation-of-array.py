class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(len(nums)):
            arr.append(nums[i])
        arr.extend(nums)    
        return arr    
        