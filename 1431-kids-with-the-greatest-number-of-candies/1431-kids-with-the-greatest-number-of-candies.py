class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = 0
        res = []

        for n in candies:
            if n > greatest:
                greatest = n
        
        for n in candies:
            if n + extraCandies >= greatest:
                res.append(True)
            else:
                res.append(False)
        
        return res