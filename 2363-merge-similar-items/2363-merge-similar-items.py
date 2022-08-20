class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d={}
        for i in items1:
            if i[0] in d:
                d[i[0]]+=i[1]
            if i[0] not in d:
                d[i[0]]=i[1]
        for i in items2:
            if i[0] in d:
                d[i[0]]+=i[1]
            if i[0] not in d:
                d[i[0]]=i[1]
        x=[]
        for i in sorted(d):
            x.append([i,d[i]])
        return x
    
        