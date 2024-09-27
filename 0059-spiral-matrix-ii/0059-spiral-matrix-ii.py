class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        l,r,t,b=0,n,0,n
        count=0

        while l < r and t < b:
            for i in range(l,r):
                count += 1
                res[t][i] = count
            t+=1

            for i in range(t,b):
                count += 1
                res[i][r-1]=count
            r-=1

            if l<r:
                for i in range(r-1,l-1,-1):
                    count += 1
                    res[b-1][i]=count
                b-=1
            
            if t<b:
                for i in range(b-1,t-1,-1):
                    count += 1
                    res[i][l]=count
                l+=1
            
        return res