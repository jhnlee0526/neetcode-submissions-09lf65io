class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]                        # 1 X 9
        cols = [set() for _ in range(9)]                        # 1 X 9
        matrix = [[set() for _ in range(3)] for _ in range(3)] # 3 x 3

        for r in range(9):
            for c in range(9):
                curVal = board[r][c]
                
                if (
                    curVal in rows[r] or
                    curVal in cols[c] or
                    curVal in matrix[r // 3][c // 3]
                ):
                    return False

                if curVal == '.':
                    continue
                
                rows[r].add(curVal)
                cols[c].add(curVal)
                matrix[r // 3][c // 3].add(curVal)
            
        return True