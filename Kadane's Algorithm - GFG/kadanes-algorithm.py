#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximu
    def maxSubArraySum(self,arr,N):
        s=[]
        for i in range(N):
            s.append(0)
        ##Your code here
        # print(s)
        s[0]=arr[0]
        for i in range(1,len(arr)):
            k=max(arr[i],arr[i]+s[i-1])
            if k>=arr[i]:
                s[i]=k
            else:
                s[i]=arr[i]
        return max(s)
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends