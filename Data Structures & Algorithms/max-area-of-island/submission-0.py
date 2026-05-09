class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0



        def dfs(i,j):
            if i < 0 or i >= m:
                return 0
            
            if j < 0 or j >= n:
                return 0
            
            if grid[i][j] != 1:
                return 0

            else:
                grid[i][j] = 0
                return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
                


            

            


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    max_area = max(max_area, area)
        return max_area