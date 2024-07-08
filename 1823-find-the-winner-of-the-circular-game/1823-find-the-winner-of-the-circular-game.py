class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ls = list(range(1, n + 1))
        idx = 0

        while n > 1:
            idx = (idx + k - 1) % n
            ls.pop(idx)
            n -= 1
        
        return ls[0]
        