class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3)!=len(s1)+len(s2):
            return False
        @cache
        def recur(i,j):
            if i==len(s1) and j==len(s2):
                return True
            c1=False
            c2=False
            if i<len(s1) and s1[i]==s3[i+j]:
                c1=recur(i+1,j)
            if j<len(s2) and s2[j]==s3[i+j]:
                c2=recur(i,j+1)
            return c1 or c2
        # print('jj')
        return recur(0,0)
        