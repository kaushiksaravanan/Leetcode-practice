from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        z=[]
        for i in range(len(nums)):
            for i in combinations(nums,i+1):
                if i not in z:
                    i=list(i)
                    i.sort()
                    z.append(i)
                if i in z:
                    continue
        y=0
        for i in z:
            y+=functools.reduce(lambda a, b: a^b, i)
        return y
        