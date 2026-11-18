class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        ans = []
        n = len(potions)
        potions.sort()
        for spell in spells:
            l,r = 0,n 
            while l < r:
                mid = (l+r)//2
                if potions[mid]*spell < success:
                    l = mid + 1
                else:
                    r = mid 
            ans.append(n -l)
        return ans

        