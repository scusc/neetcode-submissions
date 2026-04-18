# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, tree: Optional[TreeNode]) -> int:
        maxSum = tree.val

        def dfs(tree):
            if tree is None:
                return 0

            left = max(dfs(tree.left), 0)
            right = max(dfs(tree.right), 0)

            nonlocal maxSum
            maxSum = max(maxSum, left + tree.val + right)

            return tree.val + max(left, right)

        dfs(tree)
        return maxSum