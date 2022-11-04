class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        m=[str(i) for i in nums]
        k=[]
        y=''
        y=m[0]
        for i in m[1:]:
            k.append(int(y,2)%5==0)
            y+=i
        k.append(int(y,2)%5==0)
        print(y)
        return k
        