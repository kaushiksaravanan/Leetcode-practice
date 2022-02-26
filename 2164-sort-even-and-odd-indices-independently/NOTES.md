class Solution:
def sortEvenOdd(self, arr: List[int]) -> List[int]:
n=len(arr)
st=[]
en=[]
for i in range(n):
if i%2==0:
st.append(arr[i])
else:
en.append(arr[i])
st.sort()
en.sort()
e=[]
k=0
l=len(en)-1
for i in range(n):
if i%2==0:
e.append(st[k])
k+=1
else:
e.append(en[l])
l-=1
​
return e