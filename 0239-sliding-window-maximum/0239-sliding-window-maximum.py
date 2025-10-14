class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()  
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # Remove elements outside the window
            if q[0] < r - k + 1:
                q.popleft()
            
            # Append max for current window
            if r >= k - 1:
                ans.append(nums[q[0]])
        
        return ans
