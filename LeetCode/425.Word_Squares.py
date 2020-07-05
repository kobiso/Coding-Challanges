"""
- Algorithm:
1. Check the word length
2. Make an alphabet dict
3. Check possible combination

- Time complexity: O(Nx26^L), where N is the number of input words and L is the length of a single word.
- Space complexity: O(N+26) = O(N), where N is the number of input words and 26 is the number of alphabet letters.
"""

import string

class Solution:

    def wordSquares(self, words: List[str]) -> List[List[str]]:

        word_len = len(words[0]) # word length: 1~5
        if word_len == 1:
            return words
        
        word_squares = []
        apb_dict = dict((alphabet, []) for alphabet in string.ascii_lowercase)
        for word in words:
            apb_dict[word[0]].append(word)

        # Check combinations in respect to 'word'
        for first in words:
            
            for second in apb_dict[first[1]]:
                second_cand = [first, second]

                if word_len > 2:
                    for third in apb_dict[first[2]]:
                        if second[2] != third[1]:
                            continue
                        third_cand = [first, second, third]
                        
                        if word_len > 3:
                            for fourth in apb_dict[first[3]]:
                                if second[3] != fourth[1] or third[3] != fourth[2]:
                                    continue
                                fourth_cand = [first, second, third, fourth]
                                
                                if word_len > 4:
                                    for fifth in apb_dict[first[4]]:
                                        if second[4] != fifth[1] or third[4] != fifth[2] or \
                                        fourth[4] != fifth[3]:
                                            continue
                                        fifth_cand = [first, second, third, fourth, fifth]
                                        word_squares.append(fifth_cand)
                                else:
                                    word_squares.append(fourth_cand)
                        else:
                            word_squares.append(third_cand)
                else:
                    word_squares.append(second_cand)

        return word_squares
