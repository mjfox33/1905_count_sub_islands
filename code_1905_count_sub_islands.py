class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        n = len(grid2)
        m = len(grid2[0])
            
        def dfs(row, col):
            if not (0 <= row < n and 0 <= col < m and grid2[row][col] == 1):
                return 1

            grid2[row][col] = 0
            is_sub_island = grid1[row][col]
            is_sub_island &= dfs(row, col-1)
            is_sub_island &= dfs(row, col+1)
            is_sub_island &= dfs(row-1, col)
            is_sub_island &= dfs(row+1, col)

            return is_sub_island
        
        return sum(dfs(row, col) for row in range(n) for col in range(m) if grid2[row][col])