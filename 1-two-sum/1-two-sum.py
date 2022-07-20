class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        l=0
        for i in nums:
            if i in d:
                return[d[i],l]
            if i not in d:
                d[target-i]=l
            l+=1
        