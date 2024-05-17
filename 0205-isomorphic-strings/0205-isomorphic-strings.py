class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1= {}
        for i in range(len(s)):
            if not dict1.get(s[i]):
                if t[i] in dict1.values():
                    return False
                dict1[s[i]] = t[i]
            if dict1[s[i]] != t[i]:
                return False
        
        return True