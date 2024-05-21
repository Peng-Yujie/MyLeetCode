# octonary tree

from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def plusOne(s, idx):
            chs = list(s)
            if chs[idx] == '9':
                chs[idx] = '0'
            else:
                chs[idx] = str(int(chs[idx]) + 1)
            return ''.join(chs)
        
        def minusOne(s, idx):
            chs = list(s)
            if chs[idx] == '0':
                chs[idx] = '9'
            else:
                chs[idx] = str(int(chs[idx]) - 1)
            return ''.join(chs)
        
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
                    if not up in visited:
                        q.append(up)
                        visited.add(up)
                    down = minusOne(cur, j)
                    if not down in visited:
                        q.append(down)
                        visited.add(down)
                    
            steps += 1

        return -1

        
        
        

        