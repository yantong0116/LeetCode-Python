class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        for i in range(1, len(s)) : 
            temp = s[0:i]
            check = 0
            j = i
            
            while j < len(s) : 
                if s[j:j+i] != temp : 
                    check = 1
                    break
                
                j += i
                
            if check == 0 : 
                return True
        
        return False
