class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_i = nums[0]
        for i in range(1,len(nums)):
            curr = nums[i]
            while stack and curr >= stack[-1][0]:
                stack.pop()

            if stack and stack[-1][1] <curr<stack[-1][0]:
                return True
            stack.append([curr,min_i])
            min_i = min(curr,min_i)
        return False
        