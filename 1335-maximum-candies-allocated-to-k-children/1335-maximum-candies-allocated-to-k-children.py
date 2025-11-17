class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        lo, hi = 1, max(candies)
        ans = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            count = 0

            for pile in candies:
                count += pile // mid
                if count >= k:
                    break

            if count >= k:      # feasible
                ans = mid
                lo = mid + 1
            else:               # not feasible
                hi = mid - 1

        return ans
