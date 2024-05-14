class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_amount = 0

        def dfs(r, c, cur_amount):
            nonlocal max_amount

            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return
        
            cur_val = grid[r][c]
            cur_amount += cur_val
            max_amount = max(max_amount, cur_amount)

            grid[r][c] = 0
            dfs(r + 1, c, cur_amount)
            dfs(r - 1, c, cur_amount)
            dfs(r, c + 1, cur_amount)
            dfs(r, c - 1, cur_amount)
            grid[r][c] = cur_val

        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0:
                    dfs(r, c, 0)
        
        return max_amount
    
    

