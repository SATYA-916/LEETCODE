# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def help(x):
            if x==None:
                return 0
            if x.val<low or x.val>high:
                x.val=0 
            return x.val+help(x.left)+help(x.right)
        return help(root)
        