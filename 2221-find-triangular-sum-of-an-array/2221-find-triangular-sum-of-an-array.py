class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def ch(arr):
            if len(arr)<=2:
                return sum(arr)
            k=[]
            for i in range(0,len(arr)-1):
                k.append((arr[i]+arr[i+1])%10)
            return ch(k)
        return ch(nums)%10
        