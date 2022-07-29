class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            if nums[i]<=0 or nums[i]>n:
                nums[i]=n+1
        for i in range(n):
            # print(nums[i],nums,abs(nums[i]),nums[abs(nums[i])-1])
            if abs(nums[i])-1<n and nums[abs(nums[i])-1]>0:
                # nums[abs(nums[i])-1]*=-1
                nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
            # print(nums[i],nums,abs(nums[i]),nums[abs(nums[i])-1])
        print(nums)
        c=1
        for i in range(n):
            if nums[i]>0:
                return i+1
            c+=1
        return n+1
        print(nums)