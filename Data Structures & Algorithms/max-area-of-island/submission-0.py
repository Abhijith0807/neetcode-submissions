class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return(0)
        maxarea=0
        rows,cols=len(grid),len(grid[0])
        visited=set()
        def bfs(rs,cs):
            landmass=deque()
            landmass.append((rs,cs))
            visited.add((rs,cs))
            area=1
            while landmass:
                rn,cn=landmass.popleft()
                directions=[(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in directions:
                    ro,co=rn+dr,cn+dc
                    if ro in range(rows) and co in range(cols) and grid[ro][co]==1 and (ro,co) not in visited:
                        area+=1
                        landmass.append((ro,co))
                        visited.add((ro,co))
            return(area)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    maxarea=max(maxarea,bfs(r,c))
        return(maxarea)


        