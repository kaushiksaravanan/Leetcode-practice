# Definition for a binary tree node.
class node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def validateBinaryTreeNodes(self, n: int, left: List[int], right: List[int]) -> bool:
        d={}
        for i in range(n):
            d[i]=node(i)

        pos=[]
        s=set()
        for i in range(n):
            k_l=d.get(left[i],None)
            k_r=d.get(right[i],None)
            cur=d[i]
            d[i].left=k_l
            d[i].right=k_r
            s.add(left[i])
            s.add(right[i])
        for i in range(n):
            if i not in s:
                pos.append(i)


        c=0
        for ii in pos:
            visited=[]
            st=[d[ii]]
            while len(st)>0:
                print([i.val for i in st])
                k1=st.pop()
                if k1 in visited:
                    return False
                visited.append(k1.val)
                if k1.left:
                    if k1.left.val in visited:
                        return False
                    st.append(k1.left)
                if k1.right:
                    if k1.right.val in visited:
                        return False
                    st.append(k1.right)
                if len(visited)==n:
                    c+=1
        if c==1:
            return True
        else:
            return False
            print(visited)

            




        # if len(visited)!=n:
        #     return False
        # for i in left:
        #     if i!=-1 and i in right:
        #         return False
        return True
            

