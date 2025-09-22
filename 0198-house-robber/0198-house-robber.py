class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        def helper(i:int) -> int:
            if i < 0:
                return 0
            if i in self.memo:
                return self.memo[i]
            self.memo[i] = max(helper(i -1),nums[i] + helper( i -2))
            return self.memo[i]
        return helper(len(nums)-1) 