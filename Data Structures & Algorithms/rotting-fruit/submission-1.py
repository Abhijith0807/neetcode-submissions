class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        q=deque()
        visited=set()
        fresh=0
        minutes=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))
                    visited.add((r,c))
        while q and fresh:
            lq=len(q)
            directions=[(1,0),(0,1),(-1,0),(0,-1)]
            for i in range(lq):
                rt,ct=q.popleft()
                for rn,cn in directions:
                    dr,dc=rn+rt,cn+ct
                    if dr in range(rows) and dc in range(cols) and (dr,dc) not in visited and grid[dr][dc]==1:
                        fresh-=1
                        q.append((dr,dc))
                        visited.add((dr,dc))
            minutes+=1
        return minutes if fresh==0 else -1
        
