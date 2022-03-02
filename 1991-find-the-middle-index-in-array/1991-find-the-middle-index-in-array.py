class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a=sum(nums[:i])
            b=sum(nums[i+1:])
            if a==b:
                return i
        return -1