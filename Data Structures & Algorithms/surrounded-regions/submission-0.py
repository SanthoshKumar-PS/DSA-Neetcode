class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        ROWS, COLS = len(board), len(board[0])
        safe = set()
        queue = deque()
        directions = [[-1,0], [0,-1], [1,0], [0,1]]

        for i in range(ROWS):
            if board[i][0]=='O':
                queue.append((i,0))
                safe.add((i,0))
            if board[i][COLS-1]=='O':
                queue.append((i,COLS-1))
                safe.add((i,COLS-1))
        for j in range(COLS):
            if board[0][j]=='O':
                queue.append((0,j))
                safe.add((0,j))
            if board[ROWS-1][j]=='O':
                queue.append((ROWS-1,j))
                safe.add((ROWS-1,j))
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if r<0 or r==ROWS or c<0 or c==COLS or board[r][c]=='X' or (r,c) in safe:
                    continue
                queue.append((r,c))
                safe.add((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=='O' and (r,c) not in safe:
                    board[r][c]='X'
