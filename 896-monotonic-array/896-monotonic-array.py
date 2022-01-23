class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        k=[]
        k[:]=nums
        k.sort()
        print(k,nums)
        return ((nums==k) or (nums==k[::-1]))
        
        