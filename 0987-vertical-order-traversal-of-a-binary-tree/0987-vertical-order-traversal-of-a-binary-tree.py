# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d1={}
        def help(res,node,row):
            if node is None:
                return 
            if res not in d1:
                d1[res]=[[row,node.val]]
            else:
                d1[res].append([row,node.val])
            help(res-1,node.left,row+1)
            help(res+1,node.right,row+1)
            return d1
        d=help(0,root,0)
        l=[]
        print(d1)
        for key, value in sorted(d1.items()):
            value.sort()
            an=[]
            for i in value:
                an.append(i[1])
            l.append(an)
        return l
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna