# def bfs()

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n=len(edges)
        d={}
        for i in edges:
            if i[0] not in d:
                d[i[0]]=1
            if i[1] not in d:
                d[i[1]]=1
            d[i[0]]+=1
            d[i[1]]+=1
        print(d)
        for i in d:
            if d[i]==n+1:
                return i