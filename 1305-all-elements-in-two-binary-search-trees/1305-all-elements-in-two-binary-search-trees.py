# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
a=[]
def inorder(root):
    if root:
        inorder(root.left)
        a.append(root.val)
        inorder(root.right)

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        a[:]=[]
        inorder(root1)
        inorder(root2)
        a.sort()
        return a
        
        