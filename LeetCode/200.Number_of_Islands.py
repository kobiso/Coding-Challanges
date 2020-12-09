class Solution:
    def __init__(self):
        self.m = None
        self.n = None
        self.grid = None
        
    def check(self, i, j):
        if i >= self.m or j >= self.n or i < 0 or j < 0:
            return
        if self.grid[i][j] == '-1' or self.grid[i][j] == '0':
            return
        self.grid[i][j] = '-1'
        
        self.check(i-1, j)
        self.check(i, j-1)
        self.check(i+1, j)
        self.check(i, j+1)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        
        num = 0
        
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j]=="1":
                    self.check(i,j)
                    num += 1
                    
        return num
