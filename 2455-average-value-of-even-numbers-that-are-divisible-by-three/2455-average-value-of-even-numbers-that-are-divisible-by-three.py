class Solution:
    def averageValue(self, nums: List[int]) -> int:
        k=[]
        for i in nums:
            if i%2==0 and i%3==0:
                k.append(i)
        if len(k)==0:
            return 0
        return sum(k)//len(k)
        