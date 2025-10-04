class Solution:
    def isValid(self, s: str) -> bool:
            stack = []
            Map = {'(':')' ,'[':']', '{':'}'}
            for c in s:
                if c == '(' or c == '[' or c == '{':
                    stack.append(c)
                else:
                    if not stack or c != Map[stack.pop()]:
                        return False
            return False if stack else True
