class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]>=0 and abs(nums[i])<abs(nums[i-1]):
                return nums[i]
            elif i>0 and nums[i]>=0 and abs(nums[i])>abs(nums[i-1]):
                return nums[i-1]
        if nums[0]>0:
            return nums[0]
        else:
            return nums[-1]
        