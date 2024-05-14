class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_m = {}

        for ch in magazine:
            dict_m[ch] = dict_m.get(ch, 0) + 1
        
        for ch in ransomNote:
            if ch not in dict_m:
                return False
            elif dict_m[ch] < 1:
                return False
            else:
                dict_m[ch] -= 1
        
        return True