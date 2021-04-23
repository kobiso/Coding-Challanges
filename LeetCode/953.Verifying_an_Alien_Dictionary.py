from itertools import zip_longest

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_dict = {}
        for idx, cha in enumerate(order, 1):
            order_dict[cha] = idx
        
        for idx, word in enumerate(words):
            if len(words) <= idx + 1:
                break
                
            for first, second in zip_longest(words[idx], words[idx+1]):
                first_val = 0 if first is None else order_dict[first]
                second_val = 0 if second is None else order_dict[second]
                
                if first_val < second_val:
                    break
                elif first_val == second_val:
                    continue
                elif first_val > second_val:
                    return False
                
        return True
