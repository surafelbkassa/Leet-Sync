class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        A = set(nums)
        Min = 0
        for x in A:
            if x - 1 not in A:
                temp = x 
                ans = 1
                while temp+1 in A:
                    ans += 1
                    temp += 1
                Min = max(ans,Min)
        return Min
            
        