class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]>=0:
                if abs(nums[i])<abs(nums[i-1]):
                    return nums[i]
                elif abs(nums[i])>abs(nums[i-1]):
                    return nums[i-1]
        if nums[0]>0:
            return nums[0]
        else:
            return nums[-1]
        