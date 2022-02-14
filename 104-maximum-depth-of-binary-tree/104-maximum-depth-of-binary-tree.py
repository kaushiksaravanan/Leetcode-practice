# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def ma(root):
    if root:
                return 1+max(ma(root.left),ma(root.right))
    else:
            return 0
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return ma(root)