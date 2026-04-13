class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ## Stack (easy solution) - "remove extra '(' from the back"
        #### time : O(n)
        #### space: O(n)
        charList = []
        openCnt = 0 # extra '(' counts
        for char in s:
            if char == '(': 
                # '('
                charList.append(char)
                openCnt += 1
            elif char == ')' and openCnt > 0: 
                # ')' when there is '(' available
                charList.append(char)
                openCnt -= 1
            elif char != ')': 
                # regular character
                charList.append(char)

        # "remove extra '(' from the back"
        filtered = []
        for char in reversed(charList):
            if char == '(' and openCnt > 0: # removing/skipping extra '('
                openCnt -= 1
            else:
                filtered.append(char)
        
        return ''.join(reversed(filtered))
        
        
        ## Stack (optimal)
        #### time : O(n)
        #### space: O(n)
        # charList = list(s)
        # stack = [] # stack of indices
        
        # for i, char in enumerate(charList):
        #     if char == '(':
        #         stack.append(i)
        #         print(stack)
        #     elif char == ')':
        #         if len(stack) > 0:
        #             stack.pop()
        #         else:
        #             charList[i] = ''
        
        # while len(stack) > 0:
        #     charList[stack.pop()] = ''
        
        # return ''.join(charList)


        ## Without Stack (optimal)
        #### time : O(n)
        #### space: O(n) for the result string
        # openCnt = 0
        # closeCnt = 0
        
        # for char in s:
        #     if char == ')':
        #         closeCnt += 1
        
        # res = []
        # for char in s:
        #     if char == '(':
        #         if openCnt == closeCnt:
        #             continue
        #         openCnt += 1
            
        #     elif char == ')':
        #         closeCnt -= 1
        #         if openCnt == 0:
        #             continue
        #         openCnt -= 1

        #     res.append(char)
        
        # return ''.join(res)
        
