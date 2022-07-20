class Solution:
    def interpret(self, command: str) -> str:
        start = 0
        end = 0
        res = ''
        
        for i in range(len(command)) : 
            if command[i].isalpha() : 
                res += command[i]
            elif command[i] == '(' : 
                start = i
            elif command[i] == ')' : 
                end = i
                if end - start == 1 : 
                    res += 'o'
        return res