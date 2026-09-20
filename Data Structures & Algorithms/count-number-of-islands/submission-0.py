class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        islands=0
        visited=set()
        def islandmatch(rs,cs):
            if not grid:
                return(0)
            landmass=deque()
            landmass.append((rs,cs))
            visited.add((rs,cs))
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            while landmass:
                rn,cn=landmass.popleft()
                for dr,dc in directions:
                    ro,co=rn+dr,cn+dc
                    if ro in range(rows) and co in range(cols) and grid[ro][co]=='1' and (ro,co) not in visited:
                        landmass.append((ro,co))
                        visited.add((ro,co))
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visited:
                    islands+=1
                    islandmatch(r,c)
        return(islands)

