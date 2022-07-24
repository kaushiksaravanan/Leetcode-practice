s=[]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        global s
        s=[]
        arr=[]
        def f(index,nums,n,arr):
                    global s
                    if index>=n:
                        # print(s)
                        s.append(arr[:])
                        return
                    arr.append(nums[index])
                    f(index+1,nums,n,arr)
                    arr.pop()
                    f(index+1,nums,n,arr)
        print(f(0,nums,n,arr))
        return s
        
            