class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        s=set()
        arr=[]
        def f(index,nums,n,arr):
                    if index>=n:
                        # print(s)
                        t=arr[:]
                        t.sort()
                        s.add(tuple(t))
                        return
                    arr.append(nums[index])
                    f(index+1,nums,n,arr)
                    arr.pop()
                    f(index+1,nums,n,arr)
        print(f(0,nums,n,arr))
        return s
        
            