class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        
        while len(nums)>0:
            temp=[]
            d={}
            x=[]
            for i in nums:
                if i in d:
                    x.append(i)
                if i not in d:
                    d[i]=1
                    temp.append(i)
                
            print(temp,x)
            ans.append(tuple(temp.copy()))
            nums=x.copy()
        return ans
        

        