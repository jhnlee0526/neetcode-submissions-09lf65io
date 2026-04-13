class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## time : O(1) -> the size of the board is fixed. 9 x 9
        ## sapce: O(1) -> created 27, constant size.
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        """
        rows = [set(), set(), ..., set()]     # 9 sets
        cols = [set(), set(), ..., set()]     # 9 sets
        boxes = [[set(), set(), set()],
                [set(), set(), set()],
                [set(), set(), set()]]       # 3x3 sets for boxes
        """

        for r in range(9):
            for c in range(9):
                curVal = board[r][c]
                if curVal == '.':
                    continue
                
                if (
                    curVal in rows[r] or 
                    curVal in cols[c] or 
                    curVal in boxes[r // 3][c // 3]
                ):
                    return False
                
                rows[r].add(curVal)
                cols[c].add(curVal)
                boxes[r // 3][c // 3].add(curVal)
        
        return True