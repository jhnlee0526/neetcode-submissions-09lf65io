class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for each in s:
            if (
                each == "{" or
                each == "[" or
                each == "("
            ):
                stack.append(each)
            elif (
                (each == "}" and len(stack) > 0 and stack[-1] == "{") or
                (each == "]" and len(stack) > 0 and stack[-1] == "[") or
                (each == ")" and len(stack) > 0 and stack[-1] == "(")
            ): 
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
        
                