class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def depth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left_height = depth(root.left)
            right_height = depth(root.right)
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            return max(left_height, right_height) + 1

        depth(root)
        return self.max_diameter