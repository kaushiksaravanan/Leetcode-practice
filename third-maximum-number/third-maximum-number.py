class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        k=list(set(nums))
        k.sort()
        print(k)
        if len(k)>=3:
            return k[-3]
        return k[-1]