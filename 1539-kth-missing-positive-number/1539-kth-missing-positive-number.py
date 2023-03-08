class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        d=[]
        l=0
        for i in range(1,max(arr)):
            # if len(d)>=k+1:
            #     break
            if i not in arr:
                d.append(i)
        if len(d)<k:
            return max(arr)+k-len(d)
        return d[k-1]