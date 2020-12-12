class Solution:
    def __init__(self):
        self.num_route = 0
        self.height = None
        self.width = None
        
    def check_all_visit(self, grid):
        for row in grid:
            if 0 in row:
                return False
        return True
    
    def dfs(self, grid, i, j):
        
        if i >= self.height or j >= self.width or i < 0 or j < 0:
            return
        elif grid[i][j] == -1 or grid[i][j] == -2:
            return
        elif grid[i][j] == 2:
            if self.check_all_visit(grid):
                self.num_route += 1
            return
        
        undo = grid[i][j]
        grid[i][j] = -2
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        grid[i][j] = undo # undoing is necessary for backtracking

    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        # Initialization
        self.height = len(grid)
        self.width = len(grid[0])
        
        # Find the starting point
        for i_idx, row in enumerate(grid):
            if 1 in row:
                j_idx = row.index(1)
                break
        
        # Compute DFS
        self.dfs(grid, i_idx, j_idx)
        
        return self.num_route
