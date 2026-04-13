class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # bfs iteratively
        #   time :
        #   space:

        res = []

        RC, CC = len(heights), len(heights[0])
        pac, atl = set(), set()     # {(r, c), ..}
        
        def bfs(list, visits):  # iteratively
            q = deque(list)
            while q:
                qr, qc = q.popleft()
                visits.add((qr, qc))

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nextR, nextC = qr + dr, qc + dc
                    if (
                        nextR in range(RC) and
                        nextC in range(CC) and
                        (nextR, nextC) not in visits and
                        heights[nextR][nextC] >= heights[qr][qc]
                    ):
                        q.append((nextR, nextC))
                        visits.add((nextR, nextC))
            
        
        pacList = [(r, 0) for r in range(RC)] + [(0, c) for c in range(CC)]           # left + top
        atlList = [(r, CC - 1) for r in range(RC)] + [(RC - 1, c) for c in range(CC)] # right + bottom

        bfs(pacList, pac)
        bfs(atlList, atl)

        # get result
        for r in range(RC):
            for c in range(CC):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res