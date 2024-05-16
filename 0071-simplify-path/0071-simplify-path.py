class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        simplified = []

        for p in paths:
            if p == '..' and simplified:
                simplified.pop()
            elif p not in ['', '.', '..']:
                simplified.append(p)
        
        return '/' + '/'.join(simplified)
