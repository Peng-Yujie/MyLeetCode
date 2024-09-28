class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        m = Counter(words)
        res = 0
        middle = 0

        for word, count in m.items():
            reverse = word[::-1]
            if word == reverse:
                if count % 2 == 0:
                    res += count * 2
                else:
                    res += (count - 1) * 2
                    middle = 2
            else:
                if reverse in m:
                    res += min(count, m[reverse]) * 2

        return res + middle
