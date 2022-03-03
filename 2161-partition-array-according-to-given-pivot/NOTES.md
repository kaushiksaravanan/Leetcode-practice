class Solution:
def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
st=[]
en=[]
mi=[]
k=[]
for i in nums:
if i<pivot:
st.append(i)
if i>pivot:
en.append(i)
if i==pivot:
mi.append(i)
return st+mi+en