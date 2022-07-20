class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        
        for index, li in enumerate(mat) : 
            res += li[index]
            res += li[~index]
            
        if len(mat) % 2 == 1 :
            res -= mat[len(mat)//2][len(mat)//2]
        
        return res