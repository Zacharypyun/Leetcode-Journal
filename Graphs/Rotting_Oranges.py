from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque()
        fresh = 0
        minutes = 0
        row, col = len(grid), len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1
        while queue and fresh > 0:
            for _ in range(len(queue)): #len(queue) is a copy when the loop first runs doesn't update when appending
                r, c = queue.popleft()
                for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    newR, newC = r + dr, c + dc
                    if 0 <= newR < row and 0 <= newC < col and grid[newR][newC] == 1:
                        fresh -= 1
                        grid[newR][newC] = 2
                        queue.append([newR, newC])
            minutes += 1
        return minutes if fresh == 0 else -1     