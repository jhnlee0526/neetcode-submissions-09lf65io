class Solution:
    def isValid(self, s: str) -> bool:
        # stack
        #   Time : O(n)
        #   Space: O(n)

        # edge case
        if len(s) == 1:
            return False

        stack = []
        for char in s:
            if char in '[({':
                stack.append(char)
            else:
                if stack and (
                    char == ']' and stack[-1] == '[' or
                    char == ')' and stack[-1] == '(' or
                    char == '}' and stack[-1] == '{'
                ):
                    stack.pop()
                else:
                    return False
        
        return not stack
                    
