# https://leetcode.com/problems/letter-combinations-of-a-phone-number
# Runtime: 48 ms, faster than 17.55% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 13.2 MB, less than 24.24% of Python3 online submissions for Letter Combinations of a Phone Number.

import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=='':
            return []
        all_chars=list()
        letter_list=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        for i in digits:
            all_chars.append(letter_list[int(i)])
        letter_product=itertools.product(*all_chars)
        letter_product=list(map(''.join,letter_product))
        return letter_product