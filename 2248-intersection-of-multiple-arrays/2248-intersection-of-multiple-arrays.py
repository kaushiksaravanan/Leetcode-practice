class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        k=set(nums[0])
        for i in nums:
            k=k.intersection(set(i))
            print(k)
        k=list(k)
        k.sort()
        return k