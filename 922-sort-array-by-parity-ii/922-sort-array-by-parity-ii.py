class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        arr=[0]*len(nums)
        even=[]
        odd=[]
        even=[False]*len(nums)
        od=1
        ev=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                # even[i]=True
                arr[ev]=nums[i]
                ev+=2
            else:
                # odd.append(nums[i])
                arr[od]=nums[i]
                od+=2
        # for i in even:
        #     if i==True:
        #         arr.append(even.pop())
        #     else:
        #         arr.append(odd.pop())
        return arr
        