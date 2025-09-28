# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(x, Sum):
            if not x:
                return False
            Sum += x.val
            if not x.left and not x.right:
                return Sum == targetSum
            return dfs(x.left, Sum) or dfs(x.right, Sum)
        return dfs(root,0)

            
