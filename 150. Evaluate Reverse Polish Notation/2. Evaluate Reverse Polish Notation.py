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
                stack.append(int(value))
            else : 
                num2 = stack.pop()
                num1 = stack.pop()
                
                if value == '+':
                    stack.append(num1 + num2)
                elif value == '-':
                    stack.append(num1 - num2)
                elif value == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(float(num1)/num2))
        
        return stack.pop()