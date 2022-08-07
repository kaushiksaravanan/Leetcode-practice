class Solution:
    def trap(self, height: List[int]) -> int:
        def get_max_cumm(height):
            n=len(height)
            max_from_end=[0]*n
            max_from_start=[0]*n
            ans=0
            curr_max=-999
            for i in range(n):
                if height[i]>curr_max:
                    curr_max=height[i]
                    max_from_start[i]=curr_max
                else:
                    if max_from_start[i-1]!=0:
                        max_from_start[i]=max_from_start[i-1]
            return max_from_start
        n=len(height)
        start=get_max_cumm(height)
        end=get_max_cumm(height[::-1])[::-1]
        print(end,start)
        ans=0
        for i in range(n):
            ans+=min(start[i],end[i])-height[i]
        print(ans)
        return ans