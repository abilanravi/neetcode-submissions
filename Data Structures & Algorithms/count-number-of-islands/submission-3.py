class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        count = 0

        def dfs(r, c):
            if (
                r >= ROWS or c >= COLS or
                r < 0 or c < 0 or
                grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"
            for dr, dc in DIRECTIONS:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        
        return count
        