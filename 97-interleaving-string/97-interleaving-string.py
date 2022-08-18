class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        n3=len(s3)
        if n3!=n1+n2:
            return False
        d={}
        @cache
        def recur(i,j):
            if i==n1 and j==n2:
                return True
            if (i,j) in d:
                return d[(i,j)]
            c1=False
            c2=False
            if i<n1 and s1[i]==s3[i+j]:
                c1=recur(i+1,j)
            if j<n2 and s2[j]==s3[i+j]:
                c2=recur(i,j+1)
            d[(i,j)]=c1 or c2
            return d[(i,j)]
        # print('jj')
        return recur(0,0)
        