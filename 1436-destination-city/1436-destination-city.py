class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d={}
        en={}
        een={}
        for i in paths:
            if i[0] in en:
                en[i[0]]+=1
            if i[1] in d:
                d[i[1]]+=1
            if i[0] not in en:
                en[i[0]]=1
            if i[1] not in d:
                d[i[1]]=1
            
            if i[0] in een:
                een[i[0]]+=1
            if i[1] in een:
                een[i[1]]+=1
            if i[0] not in een:
                een[i[0]]=1
            if i[1] not in een:
                een[i[1]]=1
            
            
        print(d)
        print(en)
        a=[]
        for i in een:
            if een[i]==1:
                a.append(i)
        for i in a:
            if i not in en:
                return i
        return a[-1]
        for i in d:
            if d[i]==1 and i!=st:
                return i
            