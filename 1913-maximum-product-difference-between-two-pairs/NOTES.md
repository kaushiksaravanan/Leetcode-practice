class Solution:
def maxProductDifference(self, a: List[int]) -> int:
ke=0
n=len(a)
for i in range(n):
for j in range(n):
for k in range(n):
for l in range(n):
if i!=j and j!=k and k!=l and l!=i:
ke=max(ke,((a[i]*a[j])-(a[k]*a[l])))
return ke