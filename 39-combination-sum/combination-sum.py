class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backTr(ind, tar, arr):

            if tar == 0:
                ans.append(arr.copy())
                return

            if tar < 0:
                return

            for i in range(ind, len(candidates)):
                arr.append(candidates[i])

                # i → same element can be used again
                backTr(i, tar - candidates[i], arr)

                arr.pop()

        backTr(0, target, [])
        return ans