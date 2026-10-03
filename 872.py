# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# we can do dfs and check if the current node has no children
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        #print(self.leaf(root1))
        #print(self.leaf(root2))
        return self.leaf(root1) == self.leaf(root2)

    def leaf(self, root: Optional[TreeNode]) -> list(int):
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        return self.leaf(root.left) + self.leaf(root.right)
