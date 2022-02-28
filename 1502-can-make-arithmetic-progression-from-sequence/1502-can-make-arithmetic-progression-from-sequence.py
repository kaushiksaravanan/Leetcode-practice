class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(2,len(arr)):
            if arr[i-1]-arr[i]!=arr[i-2]-arr[i-1]:
                print('sfsf')
                return False
        return True
                
        