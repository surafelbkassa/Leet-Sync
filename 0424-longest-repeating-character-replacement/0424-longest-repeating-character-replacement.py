class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        ans = 0
        Max_count = 0
        Map = defaultdict(int)
        while r < len(s):   
            Map[s[r]] += 1
            Max_count = max(Max_count, Map[s[r]])
            while (r - l +1) - Max_count > k and l < r:
                Map[s[l]] -= 1
                l += 1
            ans = max(r - l + 1,ans)
            r += 1
        return ans
                    
            