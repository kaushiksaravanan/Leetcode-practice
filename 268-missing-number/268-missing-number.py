class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i=0
        nums.sort()
        while(i<len(nums)):
            if nums[i]!=i:
                return i
            else:
                i+=1
        return len(nums)
    
            
        