class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff=999999999
        prev=arr[0]
        for i in arr[1:]:
            # print(i,diff)
            diff=min(diff,abs(prev-i))
            prev=i
        k=[]
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])==diff:
                k.append([arr[i],arr[i+1]])
        print(diff)
        return k
            