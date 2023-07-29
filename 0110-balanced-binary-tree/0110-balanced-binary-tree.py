# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag=0
        def recu(root):
            nonlocal flag
            if root:
                n1=recu(root.left)
                n2=recu(root.right)
                flag=max(flag,abs(n1-n2))
                print(n1,n2,root.val,flag)
                return 1+max(n1,n2)
            else:
                return 0
        print(recu(root),flag)
        return flag<=1
            