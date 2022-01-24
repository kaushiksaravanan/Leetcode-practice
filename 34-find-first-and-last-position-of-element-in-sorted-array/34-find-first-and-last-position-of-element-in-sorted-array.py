class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        L=len(nums)
        a=[-1,-1]
        if L<=2:
            if target in nums:
                if L==2:
                    if nums[0]==target and nums[1]==target:
                        return [0,1]
                    if nums[0]==target and nums[1]!=target:
                        return [0,0]
                    if nums[0]!=target and nums[1]==target:
                        return [1,1]
                    else:
                        return [-1,-1]
                else:
                    return [0,0]
        if L==0:
            return [-1,-1]
        if nums[0]==target:
            for i in range(L):
                if nums[i]>target:
                    return [0,i-1]
        for i in range(L):
            if nums[i]<target:
                a[0]=i+1
            if nums[i]>target:
                a[1]=i-1
                break
        if nums[-1]==target and nums[-2]==target:
            a[1]=L-1
            if nums[0]==target:
                a[0]=0
            return a
        
        if nums[-1]==target and nums[-2]!=target:
            return [L-1,L-1]
        if target not in nums:
            return [-1,-1]
        # if a[0]==nums[0] and a[1]==nums[0]:
        #     return a[-]
        return a
            
                
        