class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        k=0
        for i in range(len(heights)):
            d[heights[i]]=names[i]
        print(d)
        m=[]
        for i in sorted(d,key=lambda x:x,reverse=True):
            m.append(d[i])
        return m