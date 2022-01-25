class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        ma=arr[0]
        max_i=0
        n=len(arr)
        for i in range(1,n):
            if arr[i]>=ma:
                max_i=i
                ma=arr[i]
        print(max_i,ma,n)
        # mi=0
        # for i in arr[max_i:]:
        #     if i<=mi:
        #         mi=arr[i]
        if max_i==(n-1) or max_i==0:
            return False
        temp=[]
        temp[:]=arr[:max_i+1]
        temp.sort()
        temp2=[]
        temp2[:]=arr[max_i:][::-1]
        temp2.sort()
        print(temp,arr[:max_i+1],temp2,arr[max_i:][::-1])
        if arr[:max_i+1]==temp and arr[max_i:][::-1]==temp2:
            if ((len(set(arr[:max_i+1]))==len(temp)) and (len(set(arr[max_i:][::-1]))==len(temp2))):
                return True
        return False
            
        
        
                
                
        