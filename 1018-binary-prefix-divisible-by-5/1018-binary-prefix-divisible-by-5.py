class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        k=[]
        y=str(nums[0])
        for i in nums[1:]:
            k.append(int(y,2)%5==0)
            y+=str(i)
        k.append(int(y,2)%5==0)
        return k
        