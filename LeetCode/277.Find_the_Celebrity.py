"""
Author: Byungsoo Ko
"""

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def check_cand(self, cand, n):
        for i in range(n):
            if i == cand:
                continue
            if knows(i, cand) != 1 and knows(cand, i) != 0:
                return False
        return True

    def findCelebrity(self, n: int) -> int:
        candidate_list = []
        for i in range(n):
            minus = n-1 if i-1 < 0 else i-1
            plus = 0 if i+1 >= n else i+1
            if knows(minus,i)==1 and knows(plus,i)==1 and knows(i,minus)==0 and knows(i,plus)==0:
                candidate_list.append(i)
        if not candidate_list:
            return -1
        for cand in candidate_list:
            if self.check_cand(cand, n):
                return cand
        return -1