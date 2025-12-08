class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split('/')
        ans = []
        for c in stack:
            if c == '..':
                if ans: ans.pop()
            elif c == '/' or c == '' or c == '.':
                continue 
            else:
                ans.append(c)
        return '/'+'/'.join(ans)
            

        