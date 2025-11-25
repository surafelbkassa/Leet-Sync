class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        n = len(nums)
        def DFS(i,curr):
            if i == n:
                if curr == target:
                    return 1
                else:
                    return 0
            if (i,curr) in memo:
                return memo[i,curr]

            memo[(i,curr)] = DFS(i + 1,curr + nums[i] ) + DFS(i+1,curr - nums[i])
            return memo[(i,curr)]
        return DFS(0,0)