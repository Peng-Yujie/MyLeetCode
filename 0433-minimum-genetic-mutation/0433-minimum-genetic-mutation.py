class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque()
        visited = set()

        q.append(startGene)
        visited.add(startGene)
        step = 0

        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.popleft()
                if cur == endGene:
                    return step
                
                for j in range(len(cur)):
                    for c in ['A', 'T', 'C', 'G']:
                        if cur[j] == c:
                            continue
                        neighbor = cur[:j] + c + cur[j + 1:]
                        if neighbor not in bank:
                            continue
                        if neighbor not in visited:
                            q.append(neighbor)
                            visited.add(neighbor)
            step += 1
        
        return -1