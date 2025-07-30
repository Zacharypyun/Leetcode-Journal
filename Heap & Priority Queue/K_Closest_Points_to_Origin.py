import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distance = math.sqrt((0 - point[0])**2 + (0 - point[1])**2)
            heapq.heappush(distances, (-distance, point))
        while len(distances) > k:
            heapq.heappop(distances)
        res = []
        for point in distances:
            res.append(point[1])
        return res