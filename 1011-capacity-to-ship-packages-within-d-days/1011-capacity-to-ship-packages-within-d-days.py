class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        def validate(x,days):
            day_count = 1
            curr_sum = 0

            for weight in weights:
                curr_sum += weight
                if curr_sum > x:
                    day_count += 1
                    curr_sum = weight
                    if day_count > days:
                        return False
                # else:
                #     curr_sum += weight
            return True
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low+high)//2
            if not validate(mid,days):
                low = mid + 1
            else:
                high = mid -1
        return low


                    