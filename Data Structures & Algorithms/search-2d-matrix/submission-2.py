class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # [binary search] : Flatten Matrix!
        # ❗Time: O(log(n × m)) — binary search over all elements
        # ❗Space: O(1) — uses only a few pointers (l, r, m)

        rows, cols = len(matrix), len(matrix[0])

        L, R = 0, rows * cols - 1
        while L <= R:
            m = L + (R - L) // 2    # overflow-safe version
            
            row = m // cols
            col = m % cols
            val = matrix[row][col]

            if val < target:
                L = m + 1
            elif val > target:
                R = m - 1
            else:
                return True

        return False

