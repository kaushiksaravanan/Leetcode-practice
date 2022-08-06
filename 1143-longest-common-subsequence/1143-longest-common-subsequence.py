class Solution:
    @lru_cache(None)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1=len(text1)-1
        l2=len(text2)-1
        c=0
        d={}
        def recur(l1,l2,c):
            if (l1,l2) in d:
                return d[l1,l2]
            if l1<0 or l2<0:
                return 0
            if text1[l1]==text2[l2]:
                c+=1
                return 1+recur(l1-1,l2-1,c)
            if text1[l1]!=text2[l2]:
                n1=recur(l1-1,l2,c)
                n2=recur(l1,l2-1,c)
                d[(l1,l2)]=max(n2,n1)
                return d[(l1,l2)]
        return recur(l1,l2,0)
        # print(c)
            
                
        