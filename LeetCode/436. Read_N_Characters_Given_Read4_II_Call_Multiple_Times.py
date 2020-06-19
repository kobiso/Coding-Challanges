# https://leetcode.com/explore/interview/card/google/59/array-and-strings/436/

# The read4 API is already defined for you.
# def read4(buf: List[str]) -> int:

class Solution:
    def __init__(self):
        
        self.pointer = 0
        self.full_str = ''
        
        read4_buf = ['', '', '', '']
        chars_read4 = read4(read4_buf)
        self.full_str += ''.join(read4_buf)
        
        while (chars_read4 == 4): # When the string is larger than four.
            chars_read4 = read4(read4_buf)
            self.full_str += ''.join(read4_buf[:chars_read4])            
    
    def read(self, buf: List[str], n: int) -> int:
        
        """Naive way
        First, read all string by multiple reading of 'read4'
        Second, return the result of 'n'
        When the number of characters is 'num_char', it takes complexity of O('num_char'/4) for init, and O(n) for read().
        """
        
        str_segment = self.full_str[self.pointer : self.pointer+n]
        segment_size = len(str_segment)
        buf[:segment_size] = list(str_segment)
        self.pointer += n
        return segment_size