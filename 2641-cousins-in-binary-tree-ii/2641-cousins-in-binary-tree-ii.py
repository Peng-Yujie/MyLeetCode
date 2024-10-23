# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # use BFS twice:
        #   1. calculate the sum of nodes
        #   2. update each node with the sum of its cousins
        node_queue = deque([root])
        level_sums = []

        while node_queue:
            level_sum = 0
            level_size = len(node_queue)
            for _ in range(level_size):
                current_node = node_queue.popleft()
                level_sum += current_node.val

                if current_node.left:
                    node_queue.append(current_node.left)
                if current_node.right:
                    node_queue.append(current_node.right)

            level_sums.append(level_sum)

        node_queue.append(root)
        root.val = 0  # the root has no cousins
        level = 1  # start with the second level

        while node_queue:
            level_size = len(node_queue)
            for _ in range(level_size):
                current_node = node_queue.popleft()
                l, r = 0, 0

                if current_node.left:
                    l = current_node.left.val
                if current_node.right:
                    r = current_node.right.val
                
                current_sum = l+r
                if current_node.left:
                    current_node.left.val = level_sums[level] - current_sum  # replace with diff (the value of its cousins)
                    node_queue.append(current_node.left)
                if current_node.right:
                    current_node.right.val = level_sums[level] - current_sum
                    node_queue.append(current_node.right)
            
            level += 1
        
        return root


