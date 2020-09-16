"""
Author: Byungsoo Ko
"""
from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        od = OrderedDict()
        for idx, cha in enumerate(s):
            if cha not in od.keys():
                od[cha] = idx
            else:
                od[cha] = -1
        for key, item in od.items():
            if item != -1:
                return item
        return -1
