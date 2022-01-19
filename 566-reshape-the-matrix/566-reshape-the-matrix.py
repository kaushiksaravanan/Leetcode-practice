class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        k=[]
        for i in mat:
            for j in i:
                k.append(j)
        print(k)
        fin=[]
        t=0
        if len(k)==r*c:
            for i in range(r):
                r=[]
                for j in range(c):
                    if t>=len(k):
                        break
                    else:
                        r.append(k[t])
                        t+=1
                fin.append(r)
            return fin
        return mat
        