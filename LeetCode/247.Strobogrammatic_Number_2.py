# When written using standard characters (ASCII), the numbers, 0, 1, 8 are symmetrical around the horizontal axis, and 6 and 9 are the same as each other when rotated 180 degrees. In such a system, the first few strobogrammatic numbers are:
# 0, 1, 8, 11, 69, 88, 96, 101, 111, 181, 609, 619, 689, 808, 818, 888, 906, 916, 986, 1001, 1111, 1691, 1881, 1961, 6009, 6119, 6699, 6889, 6969, 8008, 8118, 8698, 8888, 8968, 9006, 9116, 9696, 9886, 9966

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        first_list = ['0', '1', '8']
        cand_list = ['0', '1', '6', '8', '9']
        
        if n == 1:
            return first_list

        res_list = []
        half_n = n//2

        for i in range(half_n):
            if i == 0:
                res_list = cand_list[1:]
            else:
                res_list = [x+y for x in res_list for y in cand_list]

        # Rotate
        for idx, ori_str in enumerate(res_list):
            rev_str = ''
            for cha in ori_str[::-1]:
                if cha == '6':
                    cha = '9'
                elif cha == '9':
                    cha = '6'
                rev_str += cha
            res_list[idx] = ori_str + rev_str

        if n%2 == 1:
            res_list = [x[:half_n] + y + x[half_n:] for x in res_list for y in first_list]
        
        return res_list