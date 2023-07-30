# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d={}
        d_he={}
        d_ch={}
        for i in descriptions:
            d[tuple(i)]=d.get(tuple(i),0)
            d_he[i[0]]=d_he.get(i[0],0)
            d_ch[i[1]]=d_he.get(i[1],0)

        r=0
        for i in d_he:
            if i not in d_ch:
                r=i
                break
        added={}
        root=TreeNode(r)

        added[root.val]=root
        for i in d:
            if i[2]==1:
                if i[1] not in added and i[0] not in added:
                    added[i[1]]=TreeNode(i[1])
                    added[i[0]]=TreeNode(i[0])
                    added[i[0]].left=added[i[1]]
                if i[1] in added and i[0] in added:
                    added[i[0]].left=added[i[1]]

                if i[1] in added and i[0] not in added:
                    added[i[0]]=TreeNode(i[0])
                    added[i[0]].left=added[i[1]]
                if i[1] not in added and i[0] in added:
                    added[i[1]]=TreeNode(i[1])
                    added[i[0]].left=added[i[1]]
                
            if i[2]==0:
                if i[1] not in added and i[0] not in added:
                    added[i[1]]=TreeNode(i[1])
                    added[i[0]]=TreeNode(i[0])
                    added[i[0]].right=added[i[1]]
                if i[1] in added and i[0] in added:
                    added[i[0]].right=added[i[1]]
                if i[1] in added and i[0] not in added:
                    added[i[0]]=TreeNode(i[0])
                    added[i[0]].right=added[i[1]]
                if i[1] not in added and i[0] in added:
                    added[i[1]]=TreeNode(i[1])
                    added[i[0]].right=added[i[1]]

        return root
        