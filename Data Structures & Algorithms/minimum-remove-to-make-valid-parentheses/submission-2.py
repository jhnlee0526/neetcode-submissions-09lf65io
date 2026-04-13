class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
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
        openCnt = 0
        closeCnt = 0
        
        for char in s:
            if char == ')':
                closeCnt += 1
        
        res = []
        for char in s:
            if char == '(':
                if openCnt == closeCnt:
                    continue
                openCnt += 1
            
            elif char == ')':
                closeCnt -= 1
                if openCnt == 0:
                    continue
                openCnt -= 1

            res.append(char)
        
        return ''.join(res)
        
