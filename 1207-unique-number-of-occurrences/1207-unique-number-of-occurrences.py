class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m={}

        for n in arr:
            occ = m.get(n,0)
            m[n]=occ+1
        
        s=set()
        for v in m.values():
            s.add(v)
        
        return len(m) == len(s)