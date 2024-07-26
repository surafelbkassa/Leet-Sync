class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = {}
        leftPtr = 0
        for rightPtr in range(len(nums)):
            while rightPtr-leftPtr>k:
                del store[nums[leftPtr]]
                leftPtr+=1   
            if nums[rightPtr] in store:
                return True
            store[nums[rightPtr]] = 0     
        return False

        