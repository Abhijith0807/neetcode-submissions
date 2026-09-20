class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid=[[0 for i in range(n)] for j in range(m)]
        grid[0][0]=1
        for r in range(m):
            for c in range(n):
                if (r,c)!=(0,0):
                    if r-1 in range(m):
                        grid[r][c]=grid[r][c]+grid[r-1][c]
                    if c-1 in range(n):
                        grid[r][c]=grid[r][c]+grid[r][c-1]
        return(grid[m-1][n-1])
        