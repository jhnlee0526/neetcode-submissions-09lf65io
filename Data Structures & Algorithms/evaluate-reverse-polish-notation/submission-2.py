class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack
        #   time : O(n) 
        #   space: O(n)
        
        stack = [] # [token1, ..]
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                num2, num1 = int(stack.pop()), int(stack.pop())
                
                if token == '+':
                    res = num1 + num2 
                elif token == '-':
                    res = num1 - num2
                elif token == '*':
                    res = num1 * num2
                else:
                    res = int(num1 / num2)
                
                stack.append(res)

            else:
                stack.append(token)
            
        return int(stack.pop())