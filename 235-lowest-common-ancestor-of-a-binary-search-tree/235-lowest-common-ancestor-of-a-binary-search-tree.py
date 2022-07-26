# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def f(root,p,q):
    if root:
                if p.val>root.val and q.val>root.val:
                    return f(root.right,p,q)
                if p.val<root.val and q.val<root.val:
                    return f(root.left,p,q)
                else:
                    return root
            
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return f(root,p,q)
            