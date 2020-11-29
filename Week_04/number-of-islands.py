class Solution:
    def removeIslands(self, i, j, grid):
        if i < 0 or j < 0 or i > self.m - 1 or j > self.n - 1 or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.removeIslands(i - 1, j, grid)
        self.removeIslands(i, j - 1, grid)
        self.removeIslands(i + 1, j, grid)
        self.removeIslands(i, j + 1, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        if self.m == 0:
            return 0
        self.n = len(grid[0])
        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    count += 1
                    self.removeIslands(i, j, grid)
        return count
