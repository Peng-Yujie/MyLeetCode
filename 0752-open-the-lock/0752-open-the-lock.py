# octonary tree

from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def plusOne(s, idx):
            return s[:idx] + str((int(s[idx]) + 1) % 10) + s[idx + 1:]
        
        def minusOne(s, idx):
            return s[:idx] + str((int(s[idx]) - 1) % 10) + s[idx + 1:]
        
        q = deque()
        visited = set()
        deads = set(deadends)
        steps = 0    # init
        q.append('0000')
        visited.add('0000')

        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.popleft()

                if cur in deads:
                    continue
                if cur == target:
                    return steps
                
                for j in range(4):
                    up = plusOne(cur, j)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)
                    down = minusOne(cur, j)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
                    
            steps += 1

        return -1

        
        
        

        