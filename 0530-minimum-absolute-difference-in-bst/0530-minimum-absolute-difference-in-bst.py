# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def traverse(root):
            vals = []
            if root:
                vals = traverse(root.left)
                vals.append(root.val)
                vals = vals + traverse(root.right)
            return vals
        
        vals = sorted(traverse(root))
        n = len(vals)
        min_diff = float('inf')
        for i in range(n - 1):
            cur_diff = vals[i+1] - vals[i]
            if cur_diff < min_diff:
                min_diff = cur_diff
        
        return min_diff
        

