class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        """
        Time complexity: O(n), when 'n' is the length of sentences (times)        
        """

        self.sent_to_time ={}
        for idx, sentence in enumerate(sentences):
            self.sent_to_time[sentence] = times[idx]
        
        self.cur_word = ''

    def input(self, c: str) -> List[str]:
        """
        Time complexity: O(n+mlogm)
        - 'n' is the length of sentences
        - 'm' is the length of candidates
        """

        if c == '#':
            if self.cur_word in self.sent_to_time.keys():
                self.sent_to_time[self.cur_word] += 1
            else:
                self.sent_to_time[self.cur_word] = 1

            self.cur_word = ''
            return []

        self.cur_word += c
        candidates = []
        for sentence in self.sent_to_time.keys():
            if sentence.startswith(self.cur_word):
                candidates.append(sentence)

        candidates.sort(key=lambda x: (-self.sent_to_time[x], x))

        return candidates[:3]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
