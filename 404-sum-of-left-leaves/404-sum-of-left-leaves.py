# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        s=[]
        def ino(root):
            if root:
                ino(root.left)
                if root.left is not None and root.left.right is None and root.left.left is None:
                    s.append(root.left.val)
                ino(root.right)
        ino(root)
        # print(s)
        return sum(s)
