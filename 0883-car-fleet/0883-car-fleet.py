class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        fleets = 0
        stack = []
        cars.sort(reverse = True)
        for pos,speed in cars:
            time = (target - pos) / speed
            if not stack or stack[-1] < time:
                stack.append(time)
                fleets += 1
        return fleets
            

            