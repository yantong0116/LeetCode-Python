class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1
        
        for i in nums : 
            result *= i
            
        if result > 0 : 
            return 1
        elif result < 0 : 
            return -1
        else : 
            return 0
        