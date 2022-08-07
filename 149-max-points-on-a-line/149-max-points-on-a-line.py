class Solution:
    def maxPoints(self, arr: List[List[int]]) -> int:
                    inf=-9999
                    m=-9999
                    if len(arr)<=1:
                        return 1
                    for i in range(len(arr)):
                        dict_slope={}
                        for j in range(i+1,len(arr)):
                                x1,y1=arr[i]
                                x2,y2=arr[j]
                                if x2-x1!=0:
                                    slope=(y2-y1)/(x2-x1)
                                else:
                                    slope=inf
                                if slope in dict_slope:
                                        dict_slope[slope]+=1
                                if slope not in dict_slope:
                                        dict_slope[slope]=2  #two points have same slope
                        if len(dict_slope)>=1:
                            m=max(m,max(dict_slope.values()))
                    return m