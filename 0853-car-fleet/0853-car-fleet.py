class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = [(position[i],speed[i]) for i in range(len(position))]
        paired.sort(key = lambda x:x[0],reverse = True)
        stack = []
        for pos,spd in paired:
            time = (target - pos)/spd
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)
