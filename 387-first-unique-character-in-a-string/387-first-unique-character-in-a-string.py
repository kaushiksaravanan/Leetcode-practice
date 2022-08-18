class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        l=0
        for i in s:
            if i in d:
                d[i]=None
            if i not in d:
                d[i]=l
            l+=1
        print(d)
        for i in d:
            if d[i]!=None:
                return d[i]
        return -1
        #     if d[i]==1:
        #         return i
        # return -1