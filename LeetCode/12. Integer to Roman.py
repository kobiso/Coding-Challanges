# https://leetcode.com/problems/integer-to-roman
# Runtime: 64 ms, faster than 84.91% of Python3 online submissions for Integer to Roman.
# Memory Usage: 13.2 MB, less than 5.14% of Python3 online submissions for Integer to Roman.

class Solution:
    def changer(self, pos, val):
        if pos == 1:
            (F, S, T) = ('I', 'V', 'X')
        elif pos == 10:
            (F, S, T) = ('X', 'L', 'C')
        elif pos == 100:
            (F, S, T) = ('C', 'D', 'M')
        elif pos == 1000:
            F = 'M'
            
        roman_str=''
        if val >= 1 and val <= 3:
            for i in range(val): roman_str += F
        elif val == 4:
            roman_str = F+S
        elif val == 5:
            roman_str = S
        elif val >= 6 and val <= 8:
            roman_str = S
            for i in range(val-5): roman_str += F
        elif val == 9:
            roman_str = F+T
        
        return roman_str
    
    def intToRoman(self, num: int) -> str:
        out_str = ''
        for pos in [1000, 100, 10, 1]:
            val = num // pos
            if val == 0:
                continue
            else:
                out_str += self.changer(pos, val)
                num -= val*pos
                
        return out_str
        