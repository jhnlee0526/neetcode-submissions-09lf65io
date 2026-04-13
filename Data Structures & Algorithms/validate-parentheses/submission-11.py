class Solution:
    def isValid(self, s: str) -> bool:
        # stack
        #   time : O(n) 
        #   space: O(n)

        stack = []
        for each in s:
            if each in '([{':
                stack.append(each)
            else:
                if stack and (
                    each == ')' and stack[-1] == '(' or
                    each == ']' and stack[-1] == '[' or
                    each == '}' and stack[-1] == '{'
                ):
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0
