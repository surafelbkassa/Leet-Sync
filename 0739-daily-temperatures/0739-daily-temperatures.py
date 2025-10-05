class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = [0] * len(temperatures) 
        for i in range(len(temperatures)):
            while  stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = i - index 
            stack.append(i)
        return ans