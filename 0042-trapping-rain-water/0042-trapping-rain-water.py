class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        ans = 0
        l,r = 0,len(height) -1 
        maxL,maxR = height[l],height[r]
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL,height[l])
                ans += maxL - height[l]
            elif maxL >= maxR:
                r -= 1
                maxR = max(maxR,height[r])
                ans += maxR - height[r]
        return ans
                


            
