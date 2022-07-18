class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        a = y1 - y0
        b = x1 - x0
        
        for i in range(len(coordinates)) : 
            x, y = coordinates[i]
            
            if b * (y - y0) != a * (x - x0) : 
                return False
        return True