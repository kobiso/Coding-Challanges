class StringIterator:

    def __init__(self, compressedString: str):
        
        self.cha_list = []
        self.idx_num = {}
        cha_idx = 0
        cur_num = ''
        for idx, cha in enumerate(compressedString):
            # 65~90, 97~122
            if 65 <= ord(cha) <= 90 or 97 <= ord(cha) <= 122:
                if len(cur_num) != 0:
                    self.idx_num[cha_idx] = int(cur_num)
                    cur_num = ''
                    cha_idx += 1
                self.cha_list.append(cha)
            else:
                cur_num += cha
        self.idx_num[cha_idx] = int(cur_num)
        
        self.cha_idx = 0

    def next(self) -> str:
        if self.cha_idx >= len(self.idx_num):
            return ' '
        if self.idx_num[self.cha_idx]:
            self.idx_num[self.cha_idx] -= 1
            return self.cha_list[self.cha_idx]
        else:
            self.cha_idx += 1
            if self.cha_idx >= len(self.cha_list):
                return ' '
            else:
                self.idx_num[self.cha_idx] -= 1
                return self.cha_list[self.cha_idx]


    def hasNext(self) -> bool:
        if self.cha_idx >= len(self.idx_num):
            return False
        if self.idx_num[self.cha_idx]:
            return True
        else:
            if self.cha_idx + 1 >= len(self.cha_list):
                return False
            else:
                return True

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()