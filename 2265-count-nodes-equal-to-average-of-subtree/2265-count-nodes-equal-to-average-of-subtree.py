# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def help(x):
            if x is None:
                return 0,0,0
            lfsum,lfnonode,lfans=help(x.left)
            rtsum,rtnonode,rtans=help(x.right)
            su=lfsum+rtsum+x.val
            nonodes=lfnonode+rtnonode+1
            if x.val==su//nonodes:
                return su,nonodes,lfans+rtans+1
            return su,nonodes,lfans+rtans
        x,y,z=help(root)
        return z


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna