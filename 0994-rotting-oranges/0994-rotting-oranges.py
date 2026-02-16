class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        minutes = 0
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid [r][c] == 1:
                    fresh += 1
        while q and fresh > 0:
            for _ in range(len(q)):
                dr,dc = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for dx,dy in directions:
                    if 0 <= dr+dx<rows and 0<=dc+dy<cols and grid[dr+dx][dc+dy] == 1:
                        grid[dr+dx][dc+dy] = 2
                        fresh -= 1
                        q.append((dr+dx,dc+dy))
            minutes += 1
        return -1 if fresh >0 else minutes