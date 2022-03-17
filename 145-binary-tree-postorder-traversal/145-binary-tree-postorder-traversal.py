
k=[]
def fin(root):
    if root: 
        fin(root.left)
        fin(root.right)
        k.append(root.val)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r=[]
        k[:]=r
        fin(root)
        return k