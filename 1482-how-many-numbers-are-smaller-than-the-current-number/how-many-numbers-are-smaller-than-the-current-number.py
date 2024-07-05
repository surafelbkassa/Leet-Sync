class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        Smaller=[]
        
        for i in range(0,len(nums)):
            N=0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    N+=1
            Smaller.append(N)
        return Smaller


        """
        :type nums: List[int]
        :rtype: List[int]
        """
        