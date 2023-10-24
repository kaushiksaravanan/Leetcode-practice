# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue=deque()
        if root:
            ans=[root.val]
        else:
            ans=[]
        exte=[root]
        queue.append(root)
        v=[]
        while queue:
                v=[]
                for k in queue:
                    if k:
                        if k.left:
                            v.append(k.left)
                        if k.right:
                            v.append(k.right)
                try:
                    ans.append(max([i.val for i in v]))
                except:
                    return ans
                queue=v.copy()
        return ans
            
            

        