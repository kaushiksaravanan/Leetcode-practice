class Solution:
def longestPalindrome(self, s: str) -> int:
n=len(s)
d={}
for i in s:
if i in d:
d[i]+=1
if i not in d:
d[i]=1
l=0
flag=0
odds=[]
evens=[]
for i in d:
print(i,d[i])
if d[i]%2==0:
evens.append(d[i])
if d[i]%2!=0:
odds.append(d[i])
odds.sort()
odds=odds[::-1]
try:
l=odds[0]
except:
pass
for i in odds[1:]:
print(i)
l+=(i-1)
return sum(evens)+l