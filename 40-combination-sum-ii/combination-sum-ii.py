class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def BT(ind,tar,arr):
            if tar==0:
                ans.append(arr.copy())
                return
            for i in range(ind,len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>tar:
                    break
                arr.append(candidates[i])
                BT(i+1,tar-candidates[i],arr)
                arr.pop()        
        BT(0,target,[])  
        return ans  


        