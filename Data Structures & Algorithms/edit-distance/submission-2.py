class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # DP: "bottom up" with 2d grid
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for r in range(len1 + 1):
            dp[r][len2] = len1 - r

        for c in range(len2 + 1):
            dp[len1][c] = len2 - c
        
        for r in range(len1 - 1, -1, -1):
            for c in range(len2 - 1, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = 1 + min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1])
        
        return dp[0][0]

        
