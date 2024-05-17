class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        
        return list(res.values())

