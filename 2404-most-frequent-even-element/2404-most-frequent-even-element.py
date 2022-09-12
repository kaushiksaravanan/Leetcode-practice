class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i%2==0:
                if i in d:
                    d[i]+=1
                if i not in d:
                    d[i]=1
        print(d)
        k=sorted(d,key=lambda x:d[x])
        if len(k)==0:
            return -1
        key=k[-1]
        val=999999999999999
        for i in k:
            if d[i]==d[key]:
                val=min(i,val)
        return val