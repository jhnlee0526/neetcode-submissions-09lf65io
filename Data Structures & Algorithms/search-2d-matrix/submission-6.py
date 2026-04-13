class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        #   Time : O(log mn)
        #   Space: O(1)

        RC, CC = len(matrix), len(matrix[0])
        l, r = 0, RC * CC - 1
        while l <= r:
            m = l + (r - l) // 2
            
            row = m // CC
            col = m % CC

            if matrix[row][col] < target:
                l = m + 1
            elif matrix[row][col] > target:
                r = m - 1
            else:
                return True
            
        return False