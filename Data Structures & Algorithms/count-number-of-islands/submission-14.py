class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        DIR = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        count = 0

        def dfs(r, c):

            if (r in range(ROWS) and
                c in range(COLS) and 
                grid[r][c] == "1"):

                grid[r][c] = "0"

                for x, y in DIR:
                    dfs(r + x, c + y)

            else:
                return
            
        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count

        


        