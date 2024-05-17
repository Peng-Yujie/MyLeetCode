class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # return the minimum edit distance between word1[0..i] and word2[0..j]
        def dp(i, j):
            if i == -1: return j + 1
            if j == -1: return i + 1

            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)
            else:
                return min(
                    dp(i, j - 1) + 1,  # insert a char same as word2[j]
                    dp(i - 1, j) + 1,  # delete a char
                    dp(i - 1, j - 1) + 1,  # replace a char
                )
        
        return dp(len(word1) - 1, len(word2) - 1)