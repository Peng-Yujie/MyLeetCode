class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        for i in range(n):
            start, end = 0, i + 1
            while end <= n:
                word = s[start: end]
                if word in wordDict:
                    start = end
                if start == n:
                    return True
                end += 1
            start = 0
        
        return False
            


            