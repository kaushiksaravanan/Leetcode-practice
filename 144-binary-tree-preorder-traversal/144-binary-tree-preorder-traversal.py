# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
k=[]
def fin(root):
    a=""
    if root:
        a=root.val  
        k.append(a)
        fin(root.left)
        fin(root.right)
    else:
        return a
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r=[]
        k[:]=r
        fin(root)
        return k
        
        # return khttps://stackoverflow.com/a/15841685