# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
d=[]
def ino(root):
    if root:
        ino(root.left)
        d.append(root.val)
        ino(root.right)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        d[:]=[]
        ino(root)
        return d
        