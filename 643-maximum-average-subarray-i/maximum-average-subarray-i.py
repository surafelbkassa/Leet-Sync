class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum=0
        n=len(nums)
        for i in range(k):
            cur_sum+=nums[i]
        max_ave=cur_sum/k

        for j in range(k,n):
            cur_sum+=nums[j]
            cur_sum-=nums[j-k]
            ave=cur_sum/k
            max_ave=max(ave,max_ave)
        return max_ave



        