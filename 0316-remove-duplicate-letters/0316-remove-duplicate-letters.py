class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        remaining = Counter(s)
        seen = set()
        stack = []
        for c in s:
            remaining[c] -= 1
            if c in seen:
                continue
            while stack and remaining[stack[-1]] > 0 and c < stack[-1]: 
                seen.remove(stack.pop())
            seen.add(c)
            stack.append(c)
        return ''.join(stack)

        