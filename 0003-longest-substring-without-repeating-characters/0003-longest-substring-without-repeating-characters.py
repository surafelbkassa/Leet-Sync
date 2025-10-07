class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        if len(s) == 1:
            return 1
        l,r = 0,0
        seen = set()
        while r < len(s):
            if s[r] in seen:
                while l < r and s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
            else:
                seen.add(s[r])
            ans = max(ans,r-l+1)
            r+=1
        return ans
