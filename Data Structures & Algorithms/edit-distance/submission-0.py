class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # [DFS recursively]
        ## time : O(3^(len1 + len2))
        ## space: O(len1 + len2)
        '''
            Your recursive DFS function explores all possible ways to match or edit word1 into word2. At each position (p1, p2), you can:
            - Match characters (if equal): 1 recursive call
            - Else:
                Delete: move p1 + 1 
                Insert: move p2 + 1
                Replace: move both p1 + 1 and p2 + 1
            That’s up to 3 recursive paths per step.
        '''
        len1, len2 = len(word1), len(word2)

        def dfs(p1, p2):  # Recursive DFS from positions p1 in word1 and p2 in word2
            # 🛑 Base case 1: if we've reached the end of word1,
            # we need to insert the remaining characters of word2
            if p1 == len1:
                return len2 - p2

            # 🛑 Base case 2: if we've reached the end of word2,
            # we need to delete the remaining characters of word1
            if p2 == len2:
                return len1 - p1

            # ✅ If current characters match, no operation needed — move both pointers forward
            if word1[p1] == word2[p2]:
                return dfs(p1 + 1, p2 + 1)

            # ❌ Characters don't match — try all three operations:

            # Option 1: delete word1[p1] → move p1 forward
            delete_op = dfs(p1 + 1, p2)

            # Option 2: insert word2[p2] → move p2 forward
            insert_op = dfs(p1, p2 + 1)

            # Option 3: replace word1[p1] with word2[p2] → move both forward
            replace_op = dfs(p1 + 1, p2 + 1)

            # 🧮 Take the minimum of all three operations and add 1 for the current step
            return 1 + min(delete_op, insert_op, replace_op)

        # 🚀 Start DFS from the beginning of both words
        return dfs(0, 0)
