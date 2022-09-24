# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        x=[]
        def rec(root,arr):
            if root:
                
                arr.append(root.val)
                if root.left is None and root.right is None:
                    if sum(arr)==targetSum:
                        x.append(arr[:])
                # arr.pop()
                print(root.val,arr)
                rec(root.left,arr)
                
                rec(root.right,arr)
                arr.pop()

        rec(root,[])
        print(x)
        return len(x)>=1
        
        