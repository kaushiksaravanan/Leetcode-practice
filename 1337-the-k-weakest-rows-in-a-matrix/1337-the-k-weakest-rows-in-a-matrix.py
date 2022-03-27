class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d={}
        for i in range(len(mat)):
            d[i]=mat[i].count(1)
        print(d)
        e=list(sorted(d.items(), key=lambda item: item[1]))
        l=0
        y=[]
        for i in e:
            if l==k:
                break
            y.append(i[0])
            l+=1
        # print(e)
        return y