"""
Inputs:
1. grid: a 2D grid of 1's and 0's
2. 1 = land and 0 = water

Returns:
Integer: number of islands

What is an island:
1.Connecting adjacent lands horizontally or vertically
2. Surrounded by water(egdes count as water)

"""
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        rows, columns = len(grid), len(grid[0])

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"
            while queue:
                row, column = queue.popleft()
                for dr,dc in [(1,0), (-1,0), (0,1),(0,-1)]:
                    nr, nc = row + dr, column + dc
                    if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        queue.append((nr,nc))
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
        return count


