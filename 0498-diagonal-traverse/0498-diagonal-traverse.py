class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        nums = {}
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                if i + j not in nums:
                    nums[i + j] = [mat[i][j]]
                else:
                    nums[i + j].append(mat[i][j])
        
        res=[]

        for k, v in nums.items():
            if k % 2 ==0:
                for n in v[::-1]:
                    res.append(n)
            else:
                for n in v:
                    res.append(n)
        
        return res
