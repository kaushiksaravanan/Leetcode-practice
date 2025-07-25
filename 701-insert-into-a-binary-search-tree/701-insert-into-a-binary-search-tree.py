# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return TreeNode(val)
            
        def ino(root):
            if root:
                if root.val>val:
                    root.left=ino(root.left)
                else:
                    root.right=ino(root.right)
                return root
            else:
                return TreeNode(val)
        ino(root)
        return root
                
        