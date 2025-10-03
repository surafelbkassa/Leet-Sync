class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r = len(height) - 1
        ans = 0
        while l < r:
            ans = max(min(height[l],height[r])*(r - l),ans)
            if height[l] > height[r]:
                r -= 1
            elif height[l] <= height[r]:
                l += 1
        return ans
