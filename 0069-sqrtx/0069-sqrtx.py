class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        sqrt = 0
        while l <= r:
            m = (l + r) // 2
            num = m*m
            if num <= x:
                l = m + 1
                sqrt = m
            else:
                r = m - 1
        return sqrt
