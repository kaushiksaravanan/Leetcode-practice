class Solution:
    def maxProductDifference(self, l: List[int]) -> int:
        # m=[]
        # ma=-999999999
        # mi=999999999999
        # max1=-9999999
        # max2=-9999999
        # min1=99999999
        # min2=99999999
        l.sort()
        # l=0
        # for i in nums:
        #     if i<0:
        #         break
        #     l+=1
        # print(l)
        return (l[-1]*l[-2])-(l[0]*l[1])
            
        # n=len(nums)
        # for i in range(len(nums)):
        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         # m.append([nums[i]*nums[j],(i,j)])
        #         ma=max(ma,nums[i]*nums[j])
        #         mi=min(mi,nums[i]*nums[j])

        # k=sorted(m,key=lambda x:x[0],reverse=True)
        # print(k)
        # print(m)
        return ma-mi
        return k[0][0]-k[-1][0]