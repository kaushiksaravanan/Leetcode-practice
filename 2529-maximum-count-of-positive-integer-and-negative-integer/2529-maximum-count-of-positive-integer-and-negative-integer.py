class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        d={}
        po=0
        ne=0
        for i in nums:
            if i>0:
                po+=1
            if i<0:
                ne+=1
        return max(po,ne)
        