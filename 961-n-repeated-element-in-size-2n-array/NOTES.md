class Solution:
def repeatedNTimes(self, nums: List[int]) -> int:
k=len(nums)
for i in nums:
if nums.count(i)==k//2:
return i