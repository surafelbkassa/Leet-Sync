class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        def dfs(i, prev, cur):
            if i == n:
                res.append(cur)
                return
            # always allowed to place '1'
            dfs(i + 1, '1', cur + '1')
            # allowed to place '0' only if previous is not '0'
            if prev != '0':
                dfs(i + 1, '0', cur + '0')

        dfs(0, '', '')
        return res
