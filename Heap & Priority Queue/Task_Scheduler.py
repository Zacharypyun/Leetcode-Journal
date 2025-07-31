import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            if task in freq:
                freq[task] += 1
            else:
                freq[task] = 1
        max_heap = []
        for frequency in freq.values():
            heapq.heappush(max_heap, -frequency)
        time = 0
        while max_heap:
            temp = []
            for _ in range(n + 1):
                if max_heap:
                    count = heapq.heappop(max_heap)
                    if count + 1 < 0:
                        temp.append(count + 1)
                time += 1
                if not max_heap and not temp:
                    break
            for num in temp:
                heapq.heappush(max_heap, num)
        return time