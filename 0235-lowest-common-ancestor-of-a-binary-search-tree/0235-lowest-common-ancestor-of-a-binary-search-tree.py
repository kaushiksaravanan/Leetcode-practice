# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def rec(root):
            if root:
                print(root.val)
                if root.val<p.val and root.val<q.val:
                    return rec(root.right)
                elif root.val>p.val and root.val>q.val:
                    return rec(root.left)
                else:
                    return root
                
        return rec(root)