# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        def depth(root: Optional[TreeNode]) -> int: 
            if not root:
                return 0
            left_depth = depth(root.left)
            right_depth = depth(root.right)
            if (abs(left_depth - right_depth) > 1):
                self.isBalanced = False
            return max(left_depth, right_depth) + 1
        depth(root)
        return self.isBalanced