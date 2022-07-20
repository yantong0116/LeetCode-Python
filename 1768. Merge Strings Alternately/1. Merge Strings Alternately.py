class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        
        for i in range(min(len(word1), len(word2))) : 
            res += word1[i]
            res += word2[i]
        
        if len(word2) > len(word1) : 
            for j in range(i + 1, i + abs(len(word1)-len(word2)) + 1) : 
                res += word2[j]
        elif len(word1) > len(word2) : 
            for j in range(i + 1, i + abs(len(word1)-len(word2)) + 1) : 
                res += word1[j]
        return res