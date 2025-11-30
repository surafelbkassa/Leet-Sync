class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(rate):
            hours_taken = 0
            for pile in piles:
                hours_taken += math.ceil(pile/rate)
            return h >= hours_taken
        low,high = 1,max(piles)

        while low < high:
            mid = (low + high) // 2
            if not isValid(mid):
                low = mid + 1
            else:
                high = mid
        return low
