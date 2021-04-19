class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split_w = s.split(" ")
        if len(pattern) != len(split_w):
            return False

        p_dict = {}
        for p, w in zip(pattern, split_w):
            if p in p_dict.keys():
                if p_dict[p] != w:
                    return False
            elif w in p_dict.values():
                return False
            else:
                p_dict[p] = w

        return True
