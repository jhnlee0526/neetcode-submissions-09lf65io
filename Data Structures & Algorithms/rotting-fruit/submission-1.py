class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ## BFS with queue (iteratively)
        rottQ = deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rottQ.append([r, c]) # or (r, c)
            
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and rottQ:
            for i in range(len(rottQ)): ##
                r , c = rottQ.popleft()

                for dr, dc in directions:
                    nextR, nextC = r + dr, c + dc
                    
                    if (
                        nextR in range(len(grid)) and
                        nextC in range(len(grid[0])) and
                        grid[nextR][nextC] == 1
                    ):
                        grid[nextR][nextC] = 2
                        fresh -= 1
                        rottQ.append([nextR, nextC]) # or (newR, newC)
            
            time += 1
        
        return time if fresh == 0 else -1