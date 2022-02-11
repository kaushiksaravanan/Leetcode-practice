class Solution:
def hasAlternatingBits(self, n: int) -> bool:
k=bin(n)
x=0
y=0
prev=k[0]
for i in k[1:]:
if i=='0' and prev=='1':
prev=i
y+=1
if i=='1' and prev=='0':
prev=i
y+=1
x+=1
print(x,y)
return x==(y+1)