# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque()
        q.append(root)
        depth = 1

        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.popleft()
                if not cur.left and not cur.right:
                    return depth
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                
            depth += 1
        
        return depth