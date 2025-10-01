class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  
        if len(s)!= len(t):
            return False 
        S =defaultdict(int)
        T =defaultdict(int)
        for c in s:
            S[c] += 1
        for c in t:
            T[c] += 1
        return S == T
