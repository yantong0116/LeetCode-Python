class Solution(object):
    def evalRPN(self, tokens):
        
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []
        operators = {'+', '-', '*', '/'}
        
        if len(tokens) == 1 : 
            return int(tokens[0])
        
        for value in tokens : 
            if value not in operators : 
                stack.append(value)
            
            else : 
                num2 = stack.pop()
                num1 = stack.pop()
                
                if value == '/' : 
                    res = int(operator.truediv(int(num1), int(num2)))
                else : 
                    res = eval(num1 + value + num2)
                    
                stack.append(str(res))
        
        return int(stack.pop())