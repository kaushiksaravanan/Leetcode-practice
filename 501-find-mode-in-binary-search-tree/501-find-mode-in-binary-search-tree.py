# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d={}
        def uno(root):
            if root:
                uno(root.left)
                if root.val in d:
                    d[root.val]+=1
                if root.val not in d:
                    d[root.val]=1
                uno(root.right)
        uno(root)
        k=d[list(sorted(d,key=lambda x:d[x]))[::-1][0]]
        val=[]
        for i in d:
            if d[i]==k:
                val.append(i)
        print(k)
        print(d)
        return val
        