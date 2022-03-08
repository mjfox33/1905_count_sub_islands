class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        
        def get_islands(grid):
            islands = list()
            n = len(grid)
            m = len(grid[0])
            for row in range(n):
                for col in range(m):
                    if grid[row][col] == 1:
                        current_island = list()
                        dfs((row, col), grid, current_island)
                        islands.append(current_island)
            return islands


        def dfs(cell, grid, current_island):
            row, col = cell
            n = len(grid)
            m = len(grid[0])
            if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] == 0:
                return

            grid[row][col] = 0
            current_island.append((row, col))
            dfs((row, col-1), grid, current_island)
            dfs((row, col+1), grid, current_island)
            dfs((row-1, col), grid, current_island)
            dfs((row+1, col), grid, current_island)
        
        g1 = get_islands(grid1)
        g2 = get_islands(grid2)

        sub_islands = 0
        for g2_island in g2:
           for g1_island in g1:
               if all(i in g1_island for i in g2_island):
                   sub_islands += 1
        return sub_islands
