class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValid(capacity):
            days_used = 1
            current = 0
            for w in weights:
                if current + w > capacity:
                    current = 0
                    days_used += 1
                current += w
            return days >= days_used
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = (low + high) // 2
            if not isValid(mid):
                low = mid + 1
            else:
                high = mid
        return low 


        