class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        rotten_q = deque()
        fruits = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten_q.append((r,c))
                elif grid[r][c] == 1:
                    fruits.add((r,c))
        def dfs(r,c):
            if r in range(ROWS) and c in range(COLS) and (r,c) in fruits:
                fruits.remove((r,c))
                rotten_q.append((r,c))
            return
        t = 0    
        while rotten_q and fruits:
            N = len(rotten_q)
            for i in range(N):
                r,c = rotten_q.popleft()
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
            t+=1
        return t if not fruits else -1
