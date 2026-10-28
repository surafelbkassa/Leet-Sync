class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def lower_bound(t):
            n = len(nums)
            l,r = 0,n
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < t:
                    l = mid +1
                else:
                    r = mid  
            return l
        left = lower_bound(target) 
        right = lower_bound(target+1) - 1
        if left >= len(nums) or nums[left] != target: return [-1,-1]
        return [left,right]
        
        