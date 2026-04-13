class Solution:
    def numDecodings(self, s: str) -> int:
        # ✅ Top-Down DP recursively (DFS) with memoization
        #   Time : O(n) — each index is computed once
        #   Space: O(n) — for recursion stack and memo dictionary

        memo = {}               # cache, {num : count, ...}

        def dfs(i):
            # 🛑 Base cases: 
            if i == len(s):     # Reached the end of the string
                return 1        #   -> One valid decoding path
            if s[i] == '0':     # Can't decode a substring starting with '0'
                return 0

            # 🧠 Memoization (cache): makes it 'O(n) time'
            if i in memo:
                return memo[i]

            # 🔢 Decode one digit (always valid if not '0')
            res = dfs(i + 1)

            # 🔢 Decode two digits if it's between 10 and 26
            if (
                i + 1 < len(s) and                  # Ensure two digits exist
                10 <= int(s[i : i + 2]) <= 26       # Valid mapping to a letter (s[i : i + 2] is the current number)
            ):
                res += dfs(i + 2)

            # 💾 Save result in memo before returning
            memo[i] = res
            return res

        # 🚀 Start decoding from index 0
        return dfs(0)

        