class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # bfs iteratively with queue
        #   time : O(R * C), Each cell is visited at most once during BFS or final scan.
        #   space: O(R * C), Queue can store up to R*C cells in worst case.
        #       [Steps]:
        #       1. Run BFS from all border "O"s
        #       2. Temporarily mark them as "T" (safe cells)
        #       3. Flip remaining "O" to "X"
        #       4. Convert "T" back to "O"

        # edge case
        if not board or not board[0]:
            return
        
        RC, CC = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # BFS marks all connected "O" cells starting from border
        def bfs(r, c):
            q = deque([(r, c)])
            board[r][c] = 'T'

            while q:
                qr, qc = q.popleft()

                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc
                    if (
                        nr in range(RC) and
                        nc in range(CC) and
                        board[nr][nc] == "O" # still "O" (unvisited)
                    ):
                        board[nr][nc] = 'T'
                        q.append((nr, nc))


        for r in range(RC):
            for c in range(CC):
                if (
                    (r == 0 or r == RC - 1 or c == 0 or c == CC - 1) and
                    board[r][c] == "O"
                ):  
                    # start BFS from all border cells
                    # border "O" cannot be surrounded
                    bfs(r, c)


        for r in range(RC):
            for c in range(CC):
                # flip surrounded "O" -> "X"
                if board[r][c] == "O":
                    board[r][c] = "X"
                # restore temporary "T" -> "O"
                elif board[r][c] == "T":
                    board[r][c] = "O"