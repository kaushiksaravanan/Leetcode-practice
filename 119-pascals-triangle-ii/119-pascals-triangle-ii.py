class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a=[[1]]
        k=[1]
        for i in range(rowIndex):
            k=[1]
            for i in range(len(a[-1])-1):
                k.append(a[-1][i]+a[-1][1+i])
            k.append(1)
            a.append(k)
        return k
        