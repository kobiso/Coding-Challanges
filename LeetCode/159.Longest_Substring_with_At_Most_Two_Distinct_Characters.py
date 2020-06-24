class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # Time complexity: O(n)

        total_max = 0
        cur_str = ''
        seq_str = ''
        for cha in s:
            cur_str += cha

            if len(set(cur_str)) > 2:
                total_max = max(total_max, len(cur_str)-1)
                cur_str = cur_str[-2]*len(seq_str) + cha

            seq_str += cha
            if len(set(seq_str)) > 1:
                seq_str = cha
        
        return max(total_max, len(cur_str))
