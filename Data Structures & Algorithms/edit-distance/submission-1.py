class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # [DP] "bottom up" with the 2D grid
        ## time : O(len1 * len2)
        ## space: O(len1 * len2)
        '''
            word1 = "cat"  # len1 = 3
            word2 = "cut"  # len2 = 3
                
                p2 →
                ""  c   u   t
            p1 ↓
            ""  [0, 0, 0, 0]
            c   [0, 0, 0, 0]
            a   [0, 0, 0, 0]
            t   [0, 0, 0, 0]
        '''

        len1, len2 = len(word1), len(word2)

        # Create the 2D grid: dp[r][c] will hold the minimum number of edits needed to convert
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        # Fill in the last row: transforming word1[r:] into an empty string
        for r in range(len1 + 1):
            # requires deleting all remaining characters
            dp[r][len2] = len1 - r
        
        # Fill in the last column: transforming empty word1 into word2[c:]
        for c in range(len2 + 1):
            # requires inserting all remaining characters
            dp[len1][c] = len2 - c
        
        # Fill the DP table from the bottom-right corner upward
        for r in range(len1 - 1, -1, -1):
            for c in range(len2 -1, -1, -1):
                if word1[r] == word2[c]:
                    # Characters match — no edit needed, move diagonally
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    # Characters differ — consider insert, delete, or replace
                    dp[r][c] = 1 + min(
                                dp[r + 1][c], 
                                dp[r][c + 1], 
                                dp[r + 1][c + 1]
                            )
        
        # Final answer: min edits to convert full word1 to word2
        return dp[0][0]



