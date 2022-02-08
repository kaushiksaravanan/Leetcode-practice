t={}
def tfib(n):
if n in t:
return t[n]
if n==0:
return 0
elif n==1 or n==2:
return 1
else:
t[n]=tfib(n-2)+tfib(n-1)+tfib(n-3)
return t[n]
class Solution:
def tribonacci(self, n: int) -> int:
return tfib(n)