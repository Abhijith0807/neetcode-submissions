class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS = len(grid),len(grid[0])
        visit = set()
        dst = 0
        q = deque()

        def dfs(r,c):
            if r in range(ROWS) and c in range(COLS) and (r,c) not in visit and grid[r][c] != -1:
                grid[r][c] = dst
                q.append((r,c))
                visit.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        while q:
            N = len(q)
            dst+=1
            for _ in range(N):
                r,c = q.popleft()
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c-1)
                dfs(r,c+1)
