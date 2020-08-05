"""
Author: Byungsoo Ko
"""
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        
        sources = [x for _,x in sorted(zip(indexes,sources))]
        targets = [x for _,x in sorted(zip(indexes,targets))]
        indexes.sort()        
        
        new_str = ''
        last = 0
        for i in range(len(indexes)):
            start, source, target = indexes[i], sources[i], targets[i]

            if last < start:
                new_str += S[last:start]
                last = start

            if S[start:].startswith(source):
                new_str += target
                last = last + len(source)

        if last != len(S):
            new_str += S[last:]

        return new_str
