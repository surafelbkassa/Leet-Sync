class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n=len(s)
        # window=set()
        # l=0
        # res=0
        # for r in range(n):
        #     while s[r] in window:
        #         window.remove(s[l])
        #         l+=1
        #     window.add(s[r])
        #     res=max(res,r-l+1)
        # return res
        # char_set=set()
        # l=0
        # ans=0
        # for r in range(len(s)):
        #     while s[r] in char_set:
        #         char_set.remove(s[l])
        #         l+=1
        #     char_set.add(s[r])
        #     ans=max(ans,r-l+1)
        # return ans
        char = set()
        l=0
        ans =0
        for i in range(len(s)):
            while s[i] in char:
                char.remove(s[l])
                l+=1
            ans = max(ans,i - l + 1)
            char.add(s[i])
        return ans















       
            






        