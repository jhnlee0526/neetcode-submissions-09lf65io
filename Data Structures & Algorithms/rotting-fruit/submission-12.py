class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # "multi=source" bfs iteratively with queue 
        #   time : O(r * c), Each cell is processed at most once.
        #   space: O(r * c), Queue may hold all cells in worst case.

        # edge case
        if not grid or not grid[0]:
            return -1
        
        minMinutes = 0
        
        RC, CC = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        q = deque() # [(r, c), ..]
        freshFruits = 0
        for r in range(RC):
            for c in range(CC):
                if grid[r][c] == 2: # start BFS at multi rotten points
                    q.append((r, c))
                elif grid[r][c] == 1: # count fresh fruits
                    freshFruits += 1
        
        if freshFruits == 0:
            return 0

        while q and freshFruits > 0:
            minMinutes += 1

            for _ in range(len(q)): ##
                qr, qc = q.popleft()

                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc
                    if (
                        nr in range(RC) and
                        nc in range(CC) and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2    # rotten
                        freshFruits -= 1    # descrement fresh fruits
                        q.append((nr, nc))

        return minMinutes if freshFruits == 0 else -1

            
            