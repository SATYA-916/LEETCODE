from typing import Optional, List
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Use a defaultdict to avoid checking if a key exists
        d1 = collections.defaultdict(list)
        
        # We need to track both the column (col) and the row (depth)
        def help(col, row, node):
            if node is None:
                return 
            
            # Store a tuple of (row, value) in the column's list
            d1[col].append((row, node.val))
            
            # Go left: column decreases, row increases
            help(col - 1, row + 1, node.left)
            # Go right: column increases, row increases
            help(col + 1, row + 1, node.right)
            
        # 1. Start the traversal at column 0, row 0
        help(0, 0, root)
        
        # 2. Build the final sorted result AFTER the traversal is fully complete
        result = []
        
        # Sort the dictionary by column index (keys)
        for col in sorted(d1.keys()):
            # Sort the tuples in this column. 
            # Python sorts tuples by the first element (row) then the second (value).
            column_nodes = sorted(d1[col])
            
            # Extract just the values to add to our final list
            result.append([val for row, val in column_nodes])
            
        return result