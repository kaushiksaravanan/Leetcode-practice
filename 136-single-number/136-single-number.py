class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)%2!=0:
                return i
        