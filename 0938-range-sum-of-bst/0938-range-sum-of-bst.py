class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def help(x):
            if x==None:
                return 0
            if x.val<low:
                return help(x.right)
            if x.val>high:
                return help(x.left)
            return x.val+help(x.left)+help(x.right)
        return help(root)
        