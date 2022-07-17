class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        distance = float(inf)
        index = 0
        
        for i, value in enumerate(points):
            x1, y1 = value[0], value[1]
            if x == x1 or y == y1 :
                new_dist = abs(x - x1) + abs(y - y1)
                
                if new_dist < distance :
                    distance = new_dist
                    index = i
        
        if distance == float(inf):
            return -1
        return index