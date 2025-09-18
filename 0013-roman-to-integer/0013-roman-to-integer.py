class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        num={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)):
            if i+1<len(s) and num[s[i]]<num[s[i+1]]:
                res-=num[s[i]]
            else:
                res+=num[s[i]]
        return res
        
        