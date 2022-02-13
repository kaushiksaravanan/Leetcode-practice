class Solution:
def rearrangeArray(self, nums: List[int]) -> List[int]:
po=[]
ne=[]
for i in range(len(nums)):
if nums[i]>0:
po.append(nums[i])
else:
ne.append(nums[i])
e=[]
k=0
for i in range(len(nums)):
try:
e.append(po[k])
e.append(ne[k])
k+=1
except:
pass
print(e)
return e