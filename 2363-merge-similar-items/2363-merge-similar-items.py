class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d={}
        for i in items1:
            # print(d,i,i[0])
            if i[0] in d:
                d[i[0]]+=i[1]
            if i[0] not in d:
                d[i[0]]=i[1]
        # print(d)
        for i in items2:
            # print(d,i,i[0])
            if i[0] in d:
                d[i[0]]+=i[1]
            if i[0] not in d:
                d[i[0]]=i[1]
        print(d)
        x=[]
        for i in sorted(d,key=lambda x:x):
            print(i)
            x.append([i,d[i]])
        return x
    
        