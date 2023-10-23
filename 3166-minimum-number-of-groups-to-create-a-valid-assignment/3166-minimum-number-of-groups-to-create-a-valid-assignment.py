class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
       k=Counter(nums)
       ans=999999999
       min_l=k[k.most_common()[-1][0]]
       for x in range(1,min_l+1):
            count=0
            for a in k:
                f=k[a]
                xa=f//(x)
                b=(f%(x))
                if b>xa:
                    count+=9999999
                    # count+=a
                # if x-b<=a:
                count+=ceil(f / (x + 1))
                
            ans=min(ans,count)

               


       return ans
        

"""
To get the minimum number of groups needed for a number having frequency f to be assigned to groups of size x or x + 1, let a = f / (x + 1) and b = f % (x + 1).
If b == 0, then we can simply create a groups of size x + 1.
If x - b <= a, we can have a - (x - b) groups of size x + 1 and x - b + 1 groups of size x. So, in total, we have a + 1 groups.
Otherwise, it's impossible.
"""