class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        dig=0
        ele=0
        for i in nums:
            for k in str(i):
                dig+=int(k)
            ele+=i
        return abs(ele-dig)
        