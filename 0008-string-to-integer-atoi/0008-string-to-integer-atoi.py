class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # 1. Remove leading whitespace
        if not s:
            return 0
        
        # 2. Determine sign
        sign = 1
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            s = s[1:]
        
        # 3. Convert digits
        num = 0
        for char in s:
            if not char.isdigit():
                break
            num = num * 10 + int(char)
        
        num *= sign
        
        # 4. Clamp within 32-bit range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        
        return num
