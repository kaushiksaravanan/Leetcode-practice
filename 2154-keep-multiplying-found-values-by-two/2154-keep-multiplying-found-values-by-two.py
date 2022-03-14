class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        n=len(nums)
        while(original in nums):
            for i in range(n):
                if original==nums[i]:
                    original*=2
        return original
            