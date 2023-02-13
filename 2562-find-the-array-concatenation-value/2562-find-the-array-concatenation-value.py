class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        an=0
        while len(nums)>1:
            nums[0]
            an+=int((str(nums[0]))+(str(nums[-1])))
            nums.pop(0)
            nums.pop(-1)
        if len(nums)==1:
            an+=int(nums[0])
        return an

