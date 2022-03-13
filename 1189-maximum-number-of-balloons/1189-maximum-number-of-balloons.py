class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        A=[0,0,0,0,0]
        for i in text:
            if i=='b':
                A[0]+=1
            if i=='a':
                A[1]+=1
            if i=='l':
                A[2]+=1
            if i=='o':
                A[3]+=1
            if i=='n':
                A[4]+=1
        A[3]=A[3]//2
        A[2]=A[2]//2
        return min(A)
        