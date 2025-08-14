from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        row, col = len(grid), len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for rowDirection, colDirection in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                newR, newC = r + rowDirection, c + colDirection
                if 0 <= newR < row and 0 <= newC < col and grid[newR][newC] == 2147483647:
                    grid[newR][newC] = grid[r][c] + 1
                    queue.append([newR, newC])
        