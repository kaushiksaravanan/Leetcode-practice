# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mi=99999999999999
        prev=-999999999999
        def ino(root):
            nonlocal mi,prev
            if root:
                ino(root.left)
                # print(root.val,prev)
                mi=min(mi,abs(root.val-prev))
                prev=root.val
                ino(root.right)

            # return mi
        ino(root)
        return mi