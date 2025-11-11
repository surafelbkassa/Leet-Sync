class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        diff = endPos - startPos
        if abs(diff) > k or (k - abs(diff)) % 2 != 0:
            return 0
        right_steps = (k + diff) // 2
        return comb(k, right_steps) % MOD
