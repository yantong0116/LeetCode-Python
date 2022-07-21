class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ''
        i = 0
        while i < len(s) :  
            if i+2 < len(s) and s[i+2] == '#' : 
                res += chr(int(s[i])*10 + int(s[i+1]) + 96)
                i += 3
            else : 
                res += chr(int(s[i]) + 96)
                i += 1
        return res