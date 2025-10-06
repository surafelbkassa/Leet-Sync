class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prifix = 1
        suffix = 1
        ans = [1]*len(nums)
        for i in range(len(nums)):
            ans[i] *= prifix
            prifix *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= suffix
            suffix *= nums[i]
        return ans

