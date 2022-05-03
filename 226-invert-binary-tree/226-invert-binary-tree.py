# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def ino(root):
    if root:
        ino(root.right)
        ino(root.left)
        root.left,root.right=root.right,root.left
    else:
        return None
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ino(root)
        return root