class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_str = 1
        cur_str = []
        for i in range(len(s)):
            cur_str = [s[i]]
            for j in range(i+1, len(s)):
                if not s[j] in cur_str:
                    cur_str.append(s[j])
                    max_str = max(max_str, len(cur_str))
                else:
                    break
        return max_str