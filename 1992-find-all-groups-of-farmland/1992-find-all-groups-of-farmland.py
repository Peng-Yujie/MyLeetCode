class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows = len(land)
        cols = len(land[0])
        res = []

        def helper(r1, c1):
            r2, c2 = r1, c1

            while r2 < rows and land[r2][c1] == 1:
                c2 = c1
                while c2 < cols and land[r2][c2] == 1:
                    land[r2][c2] = 2
                    c2 += 1
                r2 += 1

            return [r1, c1, r2 - 1, c2 - 1]
        
        for r1 in range(rows):
            for c1 in range(cols):
                if land[r1][c1] == 1:
                    rectangle = helper(r1, c1)
                    res.append(rectangle)

        return res
        