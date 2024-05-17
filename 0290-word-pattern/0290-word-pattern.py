class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        dict1 = {}
        m, n = len(pattern), len(s)
        if m != n: return False

        for i in range(m):
            if not dict1.get(pattern[i]):
                if s[i] in dict1.values():
                    return False
                dict1[pattern[i]] = s[i]
            if dict1[pattern[i]] != s[i]:
                return False
        
        return True