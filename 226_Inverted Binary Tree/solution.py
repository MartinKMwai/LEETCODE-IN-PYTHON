class Solution:
    def invertTree(self, root: TreeNode)->TreeNode:
        #if there is no root/ no tree, return nothing
        if not root:
            return None

        #otherwise, swap the lweft and right child using a new variable
        temp = root.left 
        root.left = root.right
        root.right = temp

        #once we swap, call the function recursively to swap the trees of each child
        self.invertTree(root.left)
        self.invertTree(root.right)

        #return the root
        return root   