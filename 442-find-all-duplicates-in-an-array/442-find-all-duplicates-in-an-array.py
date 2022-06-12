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
        
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        D={}
        for i in nums:
            if i in D:
                D[i]+=1
            if i not in D:
                D[i]=1
        c=[]
        for i in D:
            if D[i]>1:
                c.append(i)
        return c