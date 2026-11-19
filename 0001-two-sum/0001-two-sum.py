class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        Map = {}
        n = len(nums) 
        for i in range(n):
            compliment = target - nums[i]
            if compliment in Map:
                return [i,Map[compliment]]
            else:
                Map[nums[i]] = i
        return []
        