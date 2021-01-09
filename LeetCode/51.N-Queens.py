class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        all_res = self.put_queens(0, n, [])
        reformat_res = []
        for queens in all_res:
            cur_list = []
            for col in queens:
                string = ''
                for i in range(n):
                    if i == col:
                        string += "Q"
                    else:
                        string += "."
                cur_list.append(string)
            reformat_res.append(cur_list)
        return reformat_res
        
    def put_queens(self, row, n, queens):
        if row == n:
            return [queens]
        res = []
        for col in range(n):
            if self.check_put(row, col, queens):
                res += self.put_queens(row+1, n, queens + [col])                
        return res
    
    def check_put(self, row, col, queens):
        for i, j in enumerate(queens):
            if j == col or row - i == abs(col - j):
                return False
        return True
