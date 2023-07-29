# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def recu(root,ma):
            if root:
                k3=0
                if root.val>=ma:
                    ma=max(ma,root.val)
                    k3=1
                k1=recu(root.left,ma)
                
                k2=recu(root.right,ma)
                
                return k1+k2+k3
            return 0
        return recu(root,-9999999)