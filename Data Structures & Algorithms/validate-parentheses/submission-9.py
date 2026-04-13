class Solution:
    def isValid(self, s: str) -> bool:
        # [Stack]

        # time : O(n)
        # space: O(n)

        stack = []
        for each in s:
            # if (
            #     each == '[' or
            #     each == '(' or
            #     each == '{'
            # ):
            if each in '([{':
                stack.append(each)
            
            elif stack and (
                    each == ']' and stack[-1] == '[' or
                    each == ')' and stack[-1] == '(' or
                    each == '}' and stack[-1] == '{'
                ):
                    stack.pop()
            else:
                return False
        
        return len(stack) == 0