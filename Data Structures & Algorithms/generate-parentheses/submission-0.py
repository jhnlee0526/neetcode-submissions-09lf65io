class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ## [Backtracking]
        #### time : O(4^n / √n)
        #### space: O(n)

        """
         - Only add an open paranthesis if open < n
         - Only add a close paranthesis if close < open
         - Stop add/removing paranthesis when open == close == n 
        """

        res = []   # Final list to store all valid combinations
        stack = [] # Stack to keep track of current parenthesis string being built

        def backtracking(openN, closeN):
            # If both open and close counts reach 'n', we have a complete valid combination
            if openN == closeN == n:
                res.append("".join(stack))   # e.g., stack = ['(', '(', ')', ')'] → result = ["(())"]
                return

            # Try to add an open parenthesis if we haven't reached the limit
            if openN < n:
                stack.append("(")            # Example: stack = ['(', '('] after two opens
                # 💡 Call backtracking with one more open
                backtracking(openN + 1, closeN)
                stack.pop()                  # Backtrack: undo last move → stack goes back to previous state

            # Try to add a closing parenthesis if it won't exceed the number of opens
            if closeN < openN:
                stack.append(")")            # Example: stack = ['(', ')'] after one open, one close
                # 💡 Call backtracking with one more close
                backtracking(openN, closeN + 1)
                stack.pop()                  # Backtrack: remove the last character

        # 🔁 Initial call: empty stack, 0 opens, 0 closes
        backtracking(0, 0)
        return res