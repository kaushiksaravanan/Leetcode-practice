class Solution:
    def calPoints(self, ops: List[str]) -> int:
        k=[]
        for i in ops:
            if i=='C':
                k.pop()
            elif i=='D':
                k.append(k[-1]*2)
            elif i=='+':
                # a=k.pop()
                k.append(k[-1]+k[-2])
            else:
                k.append(int(i))
        print(k)
        return sum(k)
                
        