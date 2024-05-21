class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start, target = '', '123450'
        for row in board:
            for n in row:
                start += str(n)
        
        neighbor = [[1, 3],[0, 4, 2], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        q = deque()
        visited = set()
        step = 0
        q.append(start)
        visited.add(start)

        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                if cur == target:
                    return step
                
                i = cur.index('0')
                for n in neighbor[i]:
                    chs = list(cur)
                    chs[i], chs[n] = chs[n], chs[i]
                    new_board = ''.join(chs)
                    if new_board not in visited:
                        q.append(new_board)
                        visited.add(new_board)
            
            step += 1
        
        return -1
