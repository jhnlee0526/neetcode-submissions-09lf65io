class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Backtracking : DFS recursively + hashset for visits
        #   Time : O(R * C * 4^n), n = len(word), RC = board size
        #   Space: O(n) for recursive stack & visits
        
        visits = set()  # {(r, c), ..}
        RC, CC = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, i):
            # base cases
            if (
                r not in range(RC) or
                c not in range(CC) or
                (r, c) in visits or
                board[r][c] != word[i]
            ):
                return False
            if i == len(word) - 1:  # reached end of word — match found!
                return True
            
            # backtracking
            # add
            visits.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i + 1):
                    return True
            # remove
            visits.remove((r, c))
            return False

        for r in range(RC):
            for c in range(CC):
                if dfs(r, c, 0):
                    return True
        return False
