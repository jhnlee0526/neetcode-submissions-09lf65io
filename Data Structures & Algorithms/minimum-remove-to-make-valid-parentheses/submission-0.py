class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Stack (optimal)
        #   time : O(n)
        #   space: O(n)
        charList = list(s)
        stack = [] # stack of indices
        
        for i, char in enumerate(charList):
            if char == '(':
                stack.append(i)
                print(stack)
            elif char == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    charList[i] = ''
        
        while len(stack) > 0:
            charList[stack.pop()] = ''
        
        return ''.join(charList)

        
