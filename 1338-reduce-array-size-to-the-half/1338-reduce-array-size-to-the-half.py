class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            if i not in d:
                d[i]=1
        n=len(arr)//2
        c=1
        for i in list(sorted(d,key=lambda x:d[x]))[::-1]:
            if d[i]>=n:
                return c
            if d[i]<=n:
                n=n-d[i]
                c+=1
        # return c
            
            
        