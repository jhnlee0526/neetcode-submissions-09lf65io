class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # BFS iteratively
        #   Time: O(R × C)
        #       → Each cell is visited at most once per ocean (Pacific & Atlantic)
        #       → Total work is proportional to number of cells
        #   Space: O(R × C)
        #       → Sets for Pacific and Atlantic visited cells
        #       → Queue can grow up to size of grid in worst case

        # base case
        if not heights or not heights[0]:
            return []
        
        res = []

        pac, atl = set(), set()     # {(r, c), ...}   

        RC, CC = len(heights), len(heights[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def bfs(starts, visits):
            q = deque(starts)         # [(r, c), ...]
            
            while q:
                qr, qc = q.popleft()
                visits.add((qr, qc))

                for dr, dc in directions:
                    nextR, nextC = dr + qr, dc + qc
                    if (
                        nextR in range(RC) and
                        nextC in range(CC) and
                        heights[nextR][nextC] >= heights[qr][qc] and
                        (nextR, nextC) not in visits
                    ):
                        q.append((nextR, nextC))
                        visits.add((nextR, nextC))

        # Initialize BFS starting points for both oceans
        pacStarts = [(0, c) for c in range(CC)] + [(r, 0) for r in range(RC)]  # Top and Left edges
        atlStarts = [(RC - 1, c) for c in range(CC)] + [(r, CC - 1) for r in range(RC)]  # Bottom and Right edges
        bfs(pacStarts, pac)
        bfs(atlStarts, atl)

        # Collect cells reachable by both oceans
        for r in range(RC):
            for c in range(CC):
                if (
                    (r, c) in pac and
                    (r, c) in atl
                ):
                    res.append([r, c])
        return res
