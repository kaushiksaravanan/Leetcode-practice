class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a=[[1]]
        for i in range(numRows-1):
            k=[1]
            for i in range(len(a[-1])-1):
                k.append(a[-1][i]+a[-1][1+i])
            k.append(1)
            a.append(k)
        return a