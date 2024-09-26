class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        m = {}

        for row in grid:
            row_tuple = tuple(row)
            m[row_tuple] = m.get(row_tuple, 0) + 1
        
        count = 0
        n = len(grid)
        for col in range(n):
            col_tuple = tuple(grid[i][col] for i in range(n))
            count += m.get(col_tuple, 0)

        return count