class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1 
            else:
                freq[i] = 1

        heap = []
        for num, f in freq.items():  
            heapq.heappush(heap, (f, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for f, num in heap]
