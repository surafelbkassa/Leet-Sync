class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # class Solution:
#   def pancakeSort(self, arr: list[int]) -> list[int]:
        ans = []

        for target in range(len(arr), 0, -1):
            index = arr.index(target)
            arr[:index + 1] = arr[:index + 1][::-1]
            arr[:target] = arr[:target][::-1]
            ans.append(index + 1)
            ans.append(target)

        return ans