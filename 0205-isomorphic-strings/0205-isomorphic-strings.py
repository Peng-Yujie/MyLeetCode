class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1, dict2 = {}, {}
        for i in range(len(s)):
            if not dict1.get(s[i]):
                dict1[s[i]] = t[i]
            if not dict2.get(t[i]):
                dict2[t[i]] = s[i]
            if dict1[s[i]] != t[i] or dict2[t[i]] != s[i]:
                return False
        
        return True