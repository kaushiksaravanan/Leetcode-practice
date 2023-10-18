class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        y=sorted(pairs,key=lambda x:x[1])
        print(y)
        l=0
        n=len(pairs)
        ans=0
        for i in range(n):
            cur=1
            prev=y[i][1]
            for j in range(i+1,n):
                if y[j][0]>prev:
                    prev=y[j][1]
                    cur+=1
            print(cur)
            ans=max(ans,cur)
        return ans
                
        