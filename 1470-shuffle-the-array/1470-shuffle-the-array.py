class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=nums[:n]
        l=0
        y=nums[n:]
        m=[]
        for i in range(2*n):
            if i%2==0:
                m.append(x.pop(0))
            else:
                m.append(y.pop(0))
        return m
            
            