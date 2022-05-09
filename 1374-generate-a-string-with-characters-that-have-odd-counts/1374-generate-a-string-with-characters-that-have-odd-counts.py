class Solution:
    def generateTheString(self, n: int) -> str:
        y='qwrtyuioplkjhgfdsazxcvbnm'
        if n%2==0:
            return y[0]*(n-1)+y[1]
        else:
            return y[0]*n