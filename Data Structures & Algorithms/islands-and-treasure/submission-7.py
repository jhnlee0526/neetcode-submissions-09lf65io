class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs (from multi-source) iteratively with queue + hashset for visits
        #   time : O(r * c) each cell is marked at most once
        #   space: O(r * c), queue and hashset

        if not grid or not grid[0]:
            return

        RC, CC = len(grid), len(grid[0])
        visits = set() # {(r, c), }
        q = deque()    # [(r, c), ]

        # enqueue all the treasure cells
        for r in range(RC):
            for c in range(CC):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visits.add((r, c))
        
        # bfs using queue
        distance = 0
        while q:
            for _ in range(len(q)):
                qr, qc = q.popleft()
                grid[qr][qc] = distance ##

                # exploring neighbors
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nextR, nextC = qr + dr, qc + dc
                    if (
                        nextR in range(RC) and
                        nextC in range(CC) and
                        (nextR, nextC) not in visits and
                        grid[nextR][nextC] != -1
                    ):
                        q.append((nextR, nextC))
                        visits.add((nextR, nextC))
            distance += 1
        

            


        

        


