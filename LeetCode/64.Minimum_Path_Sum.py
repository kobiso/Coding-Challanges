class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if x == 0 and y == 0:
                    continue
                elif x == 0:
                    grid[x][y] += grid[x][y-1]
                elif y == 0:
                    grid[x][y] += grid[x-1][y]
                else:
                    grid[x][y] += min(grid[x-1][y], grid[x][y-1])
        return grid[-1][-1]
