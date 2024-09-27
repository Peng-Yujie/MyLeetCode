# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = root.val

        def dfs(node):
            nonlocal ans

            if not node:
                return 0

            l = max(dfs(node.left), 0)
            r = max(dfs(node.right), 0)

            ans = max(node.val + l + r, ans)

            return node.val + max(l, r)

        dfs(root)

        return ans
