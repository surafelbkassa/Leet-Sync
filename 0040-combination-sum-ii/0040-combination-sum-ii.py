class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        subset = []
        res = []
        Sum = 0
        def dfs(i,subset,Sum):
            if Sum == target:
                res.append(subset.copy())
                return
            if Sum>target or i == len(candidates):
                return
            subset.append(candidates[i])
            dfs(i+1,subset,Sum+candidates[i])
            subset.pop()
            while i +1< len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1,subset,Sum)
        dfs(0,subset,0)
        return res
