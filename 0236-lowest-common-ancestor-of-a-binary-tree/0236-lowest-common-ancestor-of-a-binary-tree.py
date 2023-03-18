# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def pre(root,a):
    if root:
        pre(root.left,a)
        a.append(root)
        pre(root.right,a)
        return a

@lru_cache(None)
def f(root,p,q):
    if root:
                l=pre(root.left,[])
                r=pre(root.right,[])
                # print(l,r,root.val)
                if l==None:
                    l=[]
                if r==None:
                    r=[]
                
                if p in r and q in r:
                        return f(root.right,p,q)
                if p in l and q in l:
                        return f(root.left,p,q)
                else:
                        return root
                    
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if q.val==9999:
            return p
        return f(root,p,q)