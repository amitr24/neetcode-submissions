# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkTree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root and not subRoot: 
                return True
            if not subRoot or not root:
                return False
            if root.val != subRoot.val:
                return False
            return True and checkTree(root.left,subRoot.left) and checkTree(root.right, subRoot.right)

        if not root and not subRoot: 
            return True
        if not subRoot or not root:
            return False

        return checkTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)