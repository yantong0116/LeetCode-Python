class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        
        for i in range(len(mat)):            
            ans += mat[i][i] + mat[i][~i]
        
        if (len(mat) % 2) : 
            ans -= mat[i//2][i//2]
        
        return ans