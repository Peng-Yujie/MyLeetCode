# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        q = [root]
        res = []
        while len(q) > 0:
            cur_level = []
            sz = len(q)
            for _ in range(sz):
                cur_node = q.pop(0)
                cur_level.append(cur_node.val)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            
            res.append(cur_level)
        
        return [level[-1] for level in res]