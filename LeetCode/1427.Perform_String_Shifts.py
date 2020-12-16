class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for cur_shift in shift:
            direction, amount = cur_shift
            if direction == 0: # left
                s = s[amount:] + s[:amount]
            else: # right
                s = s[-amount:] + s[:-amount]
        return s