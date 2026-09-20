class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        visited=set()
        def wordfinder(i,r,c):
            visited.add((r,c))
            directions=[(1,0),(0,1),(-1,0),(0,-1)]
            for dr,dc in directions:
                rt,ct=r+dr,c+dc
                if rt in range(rows) and ct in range(cols) and (rt,ct) not in visited:
                    if board[rt][ct]==word[i] and i==len(word)-1:
                        return(True)
                    elif board[rt][ct]==word[i] and wordfinder(i+1,rt,ct) :
                        return(True)
            return(False)

        for r in range(rows):
            for c in range(cols):
                if board[r][c]==word[0] and len(word)==1:
                    return(True)
                elif board[r][c]==word[0] and wordfinder(1,r,c):
                    return(True)
                else:
                    visited=set()
        return(False)

        