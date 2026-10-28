class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        grp={}
        stack=[]
        for num in nums2:
            while stack and num>stack[-1]:
                smaller=stack.pop()
                grp[smaller]=num
            stack.append(num)
        result=[]    
        for num in nums1:
            result.append(grp.get(num,-1))
        return result            
                
        