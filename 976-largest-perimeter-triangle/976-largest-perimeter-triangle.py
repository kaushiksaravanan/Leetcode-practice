class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        nums.sort()
        nums[:]=nums[::-1]
        print(nums)
        for i in range(len(nums)-2):
            print(i)
            if nums[i+2]+nums[i+1]>nums[i]:
                print('ds')
                return nums[i]+nums[i+1]+nums[i+2]
        return 0