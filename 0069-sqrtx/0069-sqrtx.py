class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,x + 1
        
        while l < r:
            mid  = (l+r) // 2
            num = mid * mid
            if num > x:
                r = mid
            else:
                l = mid + 1
        return l-1

        