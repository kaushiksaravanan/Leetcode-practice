class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            elif i not in d:
                d[i]=1
        k=[]
        for i in d.items():
            if i[1]==2:
                k.append(i[0])
        return k     