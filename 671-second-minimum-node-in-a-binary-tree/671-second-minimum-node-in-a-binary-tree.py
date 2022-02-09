# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
d=[]
def ino(root):
    if root:
        ino(root.left)
        d.append(root.val)
        ino(root.right)
def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
        d[:]=[]
        ino(root)
        return d
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        k=list(set(inorderTraversal(root)))
        print(k)
        k.sort()
        if len(k)==2:
            return max(k)
        if len(k)<=1:
            return -1
        return k[1]