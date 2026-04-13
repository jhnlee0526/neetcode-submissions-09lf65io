class Solution:
    def isValid(self, s: str) -> bool:
        # using a stack
        stack = []
        
        for curChar in s:
            if curChar in '([{':
                stack.append(curChar)
            
            else:
                if (
                    curChar == ')' and stack and stack[-1] == '(' or
                    curChar == ']' and stack and stack[-1] == '[' or
                    curChar == '}' and stack and stack[-1] == '{'
                ):
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0
