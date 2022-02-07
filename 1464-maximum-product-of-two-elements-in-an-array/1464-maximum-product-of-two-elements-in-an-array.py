class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        k=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k=max(k,(nums[i]-1)*(nums[j]-1))
        return k
                
								
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)
                

        

        