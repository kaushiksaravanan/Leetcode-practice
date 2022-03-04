from itertools import permutations
class Solution:
    def minimumSum(self, num: int) -> int:
            k=999999999999
            for j in permutations(list(str(num)),4):
                for t in range(1,4):
                    r=list(j)
                    k=min(k,int("".join(r[:t]))+int("".join(r[t:])))
            return k
                
        