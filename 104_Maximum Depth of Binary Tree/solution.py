class solution:
    def maxDepth(self, root: TreeNode) -> int:
        #if there is no root, the depth is 0
        if not root:
            return 0

        #id there is a tree, then we return 1 + the maximum depth of a given subtree
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))