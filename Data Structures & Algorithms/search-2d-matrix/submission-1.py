class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # [binary search]: search row range → then search inside the row
        # ❗Time: O(log(rows) + log(cols)) — binary search twice
        # ❗Space: O(1) — no extra space used

        rows, cols = len(matrix), len(matrix[0])

        # 🔍 Step 1: Binary search to find which row could contain the target
        top, bottom = 0, rows - 1
        while top <= bottom:
            midRow = (top + bottom) // 2
            if target < matrix[midRow][0]:
                bottom = midRow - 1  # Target is smaller than row's smallest
            elif target > matrix[midRow][-1]:
                top = midRow + 1    # Target is larger than row's largest
            else:
                break               # Target must be in this row

        # 🛑 If no matching row found
        if top > bottom:
            return False

        # 🔍 Step 2: Binary search inside the selected row
        selectedRow = (top + bottom) // 2
        left, right = 0, cols - 1
        while left <= right:
            midCol = (left + right) // 2
            if target < matrix[selectedRow][midCol]:
                right = midCol - 1
            elif target > matrix[selectedRow][midCol]:
                left = midCol + 1
            else:
                return True
        return False

        
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