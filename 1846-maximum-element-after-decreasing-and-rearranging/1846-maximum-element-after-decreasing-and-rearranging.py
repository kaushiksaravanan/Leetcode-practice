class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        c=0
        n=len(arr)
        if arr[0]!=1:
            arr[0]=1
            c+=1
        prev=1
        for i in range(1,n):
            if arr[i]==prev+1 or arr[i]==prev-1 or arr[i]==prev:
                prev=arr[i]
            else:
                arr[i]=prev+1
                prev=arr[i]
                c+=1
        return max(arr)
                
            
            