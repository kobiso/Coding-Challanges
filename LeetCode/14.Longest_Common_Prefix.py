class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        sorted_list = sorted(strs, key=len)
        
        lcp = ''
        for idx in range(len(sorted_list[0])):
            if not all(sorted_list[0][idx] == string[idx] for string in sorted_list):
                break
            lcp += sorted_list[0][idx]
        
        return lcp
