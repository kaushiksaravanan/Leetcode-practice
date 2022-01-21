class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a=[]
        n=len(nums)
        for i in list(set(nums)):
            if nums.count(i)>(n//3):
                a.append(i)
        return a
        