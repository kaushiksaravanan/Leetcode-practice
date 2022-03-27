class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d={}
        for i in range(len(mat)):
            d[i]=mat[i].count(1)
        l=0
        y=[]
        for i in list(sorted(d.items(), key=lambda item: item[1])):
            if l==k:
                break
            y.append(i[0])
            l+=1
        return y