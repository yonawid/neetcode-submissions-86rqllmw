# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(node):
            # Base Case 1: Reached an empty branch -> nothing found here
            if node is None:
                return None

            # Base Case 2: Found target `p` or target `q` -> report this node upward
            if node == p or node == q:
                return node

            # Search both left and right subtrees
            left = helper(node.left)
            right = helper(node.right)

            # If both left and right found a target, `node` is the split point (LCA)!
            if left and right:
                return node

            # Otherwise, return whichever side is not None (or None if neither found anything)
            return left or right

        return helper(root)