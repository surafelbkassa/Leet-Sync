class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def validate(mid):
            
            hours = 0
            for i in range(len(piles)):
                
                hours += (piles[i] + mid - 1)//mid
                if hours > h:
                    return False
            return True
        
        low, high = 1,max(piles)
        while low <= high:
            mid = (low+high)//2
            if not validate(mid):
                low = mid + 1
            else:
                high = mid - 1
        return low
