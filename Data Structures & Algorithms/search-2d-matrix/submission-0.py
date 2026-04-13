class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # [binary search] : Flatten Matrix!
        # ❗Time: O(log(n × m)) — binary search over all elements
        # ❗Space: O(1) — uses only a few pointers (l, r, m)

        rows, cols = len(matrix), len(matrix[0])

        # Treat the matrix as a flattened 1D array with indices from 0 to rows * cols - 1
        left, right = 0, rows * cols - 1

        while left <= right:
            # Midpoint index (overflow-safe version)
            mid = left + (right - left) // 2

            # Convert 1D index 'mid' back to 2D (row, col)
            row = mid // cols       # How many full rows fit before 'mid'
            col = mid % cols        # What's left over — the column within that row

            val = matrix[row][col]  # The actual matrix value at (row, col)

            if target > val:
                left = mid + 1      # Search right half
            elif target < val:
                right = mid - 1     # Search left half
            else:
                return True         # Target found

        return False                # Target not found