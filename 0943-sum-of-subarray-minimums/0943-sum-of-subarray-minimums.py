class Solution:
    def sumSubarrayMins(self, arr):
        mod = 10**9 + 7
        n = len(arr)

        # Step 1: previous smaller (strict)
        prev = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)

        # Step 2: next smaller or equal
        nxt = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nxt[i] = stack[-1] if stack else n
            stack.append(i)

        # Step 3: contribution
        ans = 0
        for i in range(n):
            left = i - prev[i]
            right = nxt[i] - i
            ans = (ans + arr[i] * left * right) % mod

        return ans
