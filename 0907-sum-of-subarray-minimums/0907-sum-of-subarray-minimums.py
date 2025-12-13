class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)
        stack = []
        ans = 0

        for i in range(n + 1):
            cur = arr[i] if i < n else 0

            while stack and arr[stack[-1]] > cur:
                mid = stack.pop()

                left = mid - stack[-1] if stack else mid + 1
                right = i - mid

                ans += arr[mid] * left * right

            stack.append(i)

        return ans % mod
