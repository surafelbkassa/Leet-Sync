class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []#monotonically increasing 
        n = len(num)
        l = 0
        while l < n:
            while stack and k >0 and int(stack[-1]) > int(num[l]):
                stack.pop()
                k -= 1

            stack.append(num[l])
            l += 1
        
        if k > 0:
            res = ''.join(stack[:len(stack)-k]).lstrip('0')
            return '0' if not res else res
        res = ''.join(stack).lstrip('0')
        return '0' if not res else res

        