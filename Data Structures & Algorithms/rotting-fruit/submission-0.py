class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ## [BFS - Breadth First Search] grid traversal + bfs
        #### time : O(m * n) - grid traversal O(mn) + bfs O(mn)
        #### space: O(m * n)
        
        rottQ = deque()  # Queue to store rotten oranges (BFS processing)
        fresh = 0  # Counter for fresh oranges
        timeSpent = 0  # Timer for tracking minutes passed
        
        # Step 1: Initialize Queue with Rotten Oranges & Count Fresh Ones
        for row in range(len(grid)):  # Iterate through rows
            for col in range(len(grid[0])):  # Iterate through columns
                if grid[row][col] == 1:  # If it's a fresh orange, increase count
                    fresh += 1
                if grid[row][col] == 2:  # If it's a rotten orange, add to queue
                    rottQ.append([row, col])

        # Step 2: Define Directions for Adjacent Grid Movements
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # Right, Left, Down, Up
        
        # Step 3: BFS to Spread Rotting Effect
        while fresh > 0 and rottQ:  # Process until all fresh oranges are rotten or queue is empty
            for i in range(len(rottQ)):  # Process each rotten orange currently in queue
                row, col = rottQ.popleft()  # Get the first rotten orange from queue

                # Spread the rot to adjacent fresh oranges
                for dr, dc in directions:  # Loop through all possible directions
                    nextRow, nextCol = row + dr, col + dc  # Compute next position
                    if (
                        nextRow in range(len(grid))  # Ensure within bounds (rows)
                        and nextCol in range(len(grid[0]))  # Ensure within bounds (cols)
                        and grid[nextRow][nextCol] == 1  # Check if it's a fresh orange
                    ):
                        grid[nextRow][nextCol] = 2  # Mark as rotten
                        fresh -= 1  # Reduce fresh count
                        rottQ.append([nextRow, nextCol])  # Add new rotten orange to queue
            
            timeSpent += 1  # Increase time counter per BFS level
        
        # Step 4: Return total minutes taken, or -1 if some oranges remain fresh
        return timeSpent if fresh == 0 else -1
        
