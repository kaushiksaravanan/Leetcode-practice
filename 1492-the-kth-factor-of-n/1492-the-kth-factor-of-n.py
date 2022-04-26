class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ke=[]
        for i in range(1,n+1):
            if n%i==0:
                ke.append(i)
        if len(ke)>k-1:
            return ke[k-1]
        else:
            return -1