class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        visited=set()
        q=deque()
        dst=0
        def add_tre(dr,dc):
            if dr in range(rows) and dc in range(cols) and (dr,dc) not in visited and grid[dr][dc]!=-1:
                grid[dr][dc]=dst
                visited.add((dr,dc))
                q.append((dr,dc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
                    visited.add((r,c))
        while q:
            lq=len(q)
            dst+=1
            for i in range(lq):
                rt,ct=q.popleft()
                add_tre(rt+1,ct)
                add_tre(rt,ct+1)
                add_tre(rt-1,ct)
                add_tre(rt,ct-1)

        