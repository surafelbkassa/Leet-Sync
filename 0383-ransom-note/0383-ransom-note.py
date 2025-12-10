class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rcount = Counter(ransomNote)
        mcount = Counter(magazine)
        for c in ransomNote:
            if c not in mcount or rcount[c] > mcount[c]:
                return False
        return True

        