class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        seen = set()
        for i in range(len(nums)):
            l,r = i + 1,len(nums)-1
            compelement = -nums[i]
            while l < r and r < len(nums):
                if nums[l] + nums[r]>compelement:
                    r -= 1
                elif  nums[l] + nums[r] < compelement:
                    l += 1
                else:
                    if (nums[i],nums[l],nums[r]) not in seen:
                        ans.append([nums[i],nums[l],nums[r]])
                        seen.add((nums[i],nums[l],nums[r]))
                    l += 1
        return ans
                
