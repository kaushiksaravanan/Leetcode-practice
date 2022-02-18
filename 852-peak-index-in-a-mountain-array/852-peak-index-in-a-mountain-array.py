class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        prev=arr[0]
        k=0
        for i in arr[1:]:
            if prev<i:
                k+=1
                prev=i
            else:
                break
        return k