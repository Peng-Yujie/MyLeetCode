# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = deque()
        q.append(root)
        res = []
        left_to_right = True
        
        while q:
            sz = len(q)
            cur = []
            left_to_right = not left_to_right
            for _ in range(sz):
                node = q.popleft()
                cur.append(node.val)
                if left_to_right:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
                    
            res.append(cur)

        return res