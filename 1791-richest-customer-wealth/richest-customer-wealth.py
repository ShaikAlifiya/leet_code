class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        arr=[]
        for i in range(len(accounts)):
            arr.append(sum(accounts[i]))
        return max(arr)    


       
        