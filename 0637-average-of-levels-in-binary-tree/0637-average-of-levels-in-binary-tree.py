# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []

        q = deque()
        q.append(root)
        res = []

        while q:
            sz = len(q)
            total, count = 0, 0
            for _ in range(sz):
                node = q.popleft()
                if node:
                    total += node.val
                    count += 1
                    q.append(node.left)
                    q.append(node.right)
            
            if count != 0:
                res.append(total/count)
        
        return res
