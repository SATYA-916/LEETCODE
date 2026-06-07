# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        s=set()
        for i in descriptions:
            s.add(i[1])
        for i in descriptions:
            if i[0] not in s:
                st=i[0]
        d={}
        for i in descriptions:
            if i[0] not in d:
                x=TreeNode(i[0])
            if i[0] in d:
                x=d[i[0]]
            if i[1] not in d:
                y=TreeNode(i[1])
            if i[1] in d:
                y=d[i[1]]
            if i[2]:
                x.left=y
            else:
                x.right=y
            d[i[0]]=x
            d[i[1]]=y
        return d[st]
            
