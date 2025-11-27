class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:     
        left = self.binary(nums,target,True)  
        right =self.binary(nums,target,False)
        return [left, right]
    def binary(self,nums,target,leftbais):  
        l = 0
        r = len(nums) - 1
        i = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                i = mid
                #looking for the most left
                if leftbais:
                    r = mid - 1
                #looking for the most right 
                else:
                    l = mid + 1
        return i
