class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map={}
        for i,num in enumerate(nums):
            complement = target - nums[i]
            if complement in num_map:
                return [num_map[target - nums[i]],i]
            num_map[num] = i
       