# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def ino(root):
    if root:
        root.right=ino(root.right)
        root.left=ino(root.left)
        root.left,root.right=root.right,root.left
        return root
    else:
        return None
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ino(root)
        return root