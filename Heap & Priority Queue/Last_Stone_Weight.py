import  heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            max_heap.append(-stone)
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)
            if stone1 != stone2:
                heapq.heappush(max_heap, -abs(stone1 - stone2))
        if len(max_heap) == 1:
            return -max_heap[0]
        else:
            return 0
