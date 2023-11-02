# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def ino(root):
            nonlocal ans
            if root:
                def rec(c,root,sum):
                    if root:
                        k1,k2=rec(c+1,root.left,sum)
                        k3,k4=rec(c+1,root.right,sum)
                        return (k1+k3+1,k2+k4+root.val)
                    else:
                        return (0,0)
                
                ino(root.left)
                a,b=rec(-1,root,sum=0)
                print(a,b)
                # a+=root.val
                # b-=1
                if a!=0 and b//a==root.val:
                    ans+=1
                ino(root.right)
        ino(root)
        return ans
            


        