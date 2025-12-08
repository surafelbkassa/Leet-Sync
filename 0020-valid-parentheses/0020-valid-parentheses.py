class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = {')':'(' , '}':'{', ']':'['}
        for c in s:
            if c in ('(','{','['):
                stack.append(c)
            else:
                if not stack and c not in ('(','{','['):
                    return False
                if stack and stack.pop() != Map[c]:
                    return False
        return True if not stack else False
        