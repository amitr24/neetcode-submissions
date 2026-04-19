class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            return max(depth(root.left), depth(root.right)) + 1

        
        def diameter(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left_height = depth(root.left)
            right_height = depth(root.right)
            curr_diameter = left_height + right_height
            return max(curr_diameter, diameter(root.left), diameter(root.right))
        
        return diameter(root)