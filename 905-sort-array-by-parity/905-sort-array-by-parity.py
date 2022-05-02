class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        while(i<j):
            if nums[j]%2==0 and nums[i]%2!=0:
                nums[j],nums[i]=nums[i],nums[j]
            if nums[j]%2!=0:
                j-=1
            if nums[i]%2==0:
                i+=1
        return nums