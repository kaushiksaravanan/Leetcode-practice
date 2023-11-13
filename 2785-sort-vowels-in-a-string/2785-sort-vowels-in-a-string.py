class Solution:
    def sortVowels(self, s: str) -> str:
        r='aAeEiIoOuU'
        ans=''
        ind=[0]*len(s)
        v=[]
        for i,d in enumerate(s):
            if d in r:
                v.append(d)
                ind[i]=1
            else:
                ind[i]=d
        v.sort()
        print(v)
        ans=''
        l=0
        print(ind)
        for ii,i in enumerate(ind):
            if i==1:
                ind[ii]=v[l]
                l+=1
        print(ind)
        return "".join(ind)


        return ans