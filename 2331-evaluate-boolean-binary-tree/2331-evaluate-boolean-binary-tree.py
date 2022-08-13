# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def pre(root):
    if root:
        print(root.val)
        if root.left and root.right:
            if root.val==2:
                n1=pre(root.right)
                n2=pre(root.left)
                print(n1,n2,'or')
                return n1 or n2
            else:
                n1=pre(root.right)
                n2=pre(root.left)
                print(n1,n2,'and')
                return n1 and n2
        elif root.left:
            return pre(root.left)
        elif root.right:
            return pre(root.right)
        else:
            return root.val
        # return root.val
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return pre(root)
        