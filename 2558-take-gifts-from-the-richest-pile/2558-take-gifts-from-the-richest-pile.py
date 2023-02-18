class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        a=0
        for i in range(k):
            ma=-999
            for i in gifts:
                if i>ma:
                    ma=i
            for i in range(len(gifts)):
                if gifts[i]==ma:
                    m=math.floor(ma**0.5)
                    gifts[i]=m
                    break
                    
        print(*gifts)
        return sum(gifts)