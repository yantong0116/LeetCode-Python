class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0) = coordinates[0]
        (x1, y1) = coordinates[1]
        
        if x0 == x1 : 
            line = 'x'
        else : 
            line = (y1 - y0)/(x1 - x0)
        
        for i in range(2, len(coordinates)) : 
            (x2, y2) = coordinates[i]
            
            if x2 == x0 : 
                if line != 'x' : 
                    return False
            elif (y2 - y0)/(x2 - x0) != line : 
                return False
            
        return True