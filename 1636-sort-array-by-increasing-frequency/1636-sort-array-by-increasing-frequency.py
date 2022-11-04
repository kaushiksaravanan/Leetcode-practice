class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        k={}
        for i in nums:
            if i in k:
                k[i]+=1
            if i not in k:
                k[i]=1
        m=sorted(k,key=lambda x:(k[x],-x))
        print(m)
        a=[]
        for i in m:
            for l in range(k[i]):
                a.append(i)
        return a