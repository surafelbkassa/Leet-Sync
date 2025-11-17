class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can(t):
            total = 0
            for r in ranks:
                total += int((t // r) ** 0.5)
                if total >= cars:
                    return True
            return False

        # max possible time: worst mechanic repairs all cars
        left, right = 0, max(ranks) * (cars ** 2)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
