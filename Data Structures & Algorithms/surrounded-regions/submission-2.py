class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS = len(board),len(board[0])
        edge_O = set()
        q = deque()
        for c in range(COLS):
            if board[0][c]=='O' and (0,c) not in edge_O:
                edge_O.add((0,c))
                q.append((0,c))
            if board[ROWS-1][c]=='O' and (ROWS-1,c) not in edge_O:
                edge_O.add((ROWS-1,c))
                q.append((ROWS-1,c))
        for r in range(ROWS):
            if board[r][0]=='O' and (r,0) not in edge_O:
                edge_O.add((r,0))
                q.append((r,0))
            if board[r][COLS-1]=='O' and (r,COLS-1) not in edge_O:
                edge_O.add((r,COLS-1))
                q.append((r,COLS-1))
        def dfs(r,c):
            if r in range(ROWS) and c in range(COLS) and (r,c) not in edge_O and board[r][c] == 'O':
                edge_O.add((r,c))
                q.append((r,c))
        while q:
            N = len(q)
            for i in range(N):
                r,c  = q.popleft()
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        for r in range(1,ROWS-1):
            for c in range(1,COLS-1):
                if (r,c) not in edge_O and board[r][c] == 'O':
                    board[r][c] = 'X'
        
