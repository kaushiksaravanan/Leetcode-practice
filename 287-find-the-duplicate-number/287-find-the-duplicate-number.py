class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                return i
            if i not in d:
                d[i]=1
            