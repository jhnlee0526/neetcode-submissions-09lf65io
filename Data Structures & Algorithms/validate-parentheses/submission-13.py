class Solution:
    def isValid(self, s: str) -> bool:
        #   Time : O(n) - visits each char in s
        #   Space: O(n) - stack

        stack = []
        for each in s:
            if each in '([{':
                stack.append(each)
            else:
                if stack and (  ##
                    each == ')' and stack[-1] == '(' or
                    each == ']' and stack[-1] == '[' or
                    each == '}' and stack[-1] == '{'
                ):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
                    
                    
