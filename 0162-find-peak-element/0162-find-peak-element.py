class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = float('-inf')
        for num in nums:
            if num > n:
                n = num
        return nums.index(n)
        