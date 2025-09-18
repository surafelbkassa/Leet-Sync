class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        num_map={}
        for i,num in enumerate(nums):
            compliment=target-num
            if  compliment in num_map:
                return [num_map[compliment],i]
            num_map[num]=i
        return []
        
















        