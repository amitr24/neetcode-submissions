# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def switch_children (self, root: Optional[TreeNNode]):
            if not root:
                return root
            temp = root.right
            root.right = root.left
            root.left = temp
            switch_children(self, root.left)
            switch_children(self, root.right)
            return root

        return switch_children(self, root)