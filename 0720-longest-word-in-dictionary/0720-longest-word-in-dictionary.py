class Solution:
    def longestWord(self, words: List[str]) -> str:
        valid = set()
        words.sort()
        best = ""
        for word in words:
            if len(word) == 1:
                valid.add(word)
                if len(best) < len(word):
                    best = word
            elif word[:-1] in valid:
                valid.add(word)
                if len(best) < len(word):
                    best = word
        return best
        
                
        