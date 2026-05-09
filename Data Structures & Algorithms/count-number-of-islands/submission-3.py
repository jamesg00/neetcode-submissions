class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])

        #given a position traverse and
        #mark entinre land as water (0)
        def dfs(i,j):
            #edge cases

            #if row index is too high
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return 
            else:
                grid[i][j] = '0'
                #right
                dfs(i, j+1)
                #left
                dfs(i+1, j)
                #down
                dfs(i, j-1)
                #up
                dfs(i-1, j)


            

        islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i,j)
        return islands

        

            




        