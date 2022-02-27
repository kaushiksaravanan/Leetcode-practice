class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid=[]
        for i in points:
            if i[0]==x or i[1]==y:
                valid.append(i)
        kee=9999999999999
        ke=[]
        # print(valid)
        for i in range(len(valid)):
            a=valid[i][0]
            b=valid[i][1]
            ke.append([points.index(valid[i]),abs(x-a)+abs(y-b)])
        # print(ke)
        if len(valid)==1:
            # r=sorted(ke, key=lambda x[0]: x.modified, reverse=True)
            return points.index(valid[0])
        if len(valid)==0:
            return -1   
        try:        
            r=min(ke)
            r= sorted(ke, key=lambda x:x[1])
            k=r[0][1]
            print(r,k)
            rr=0
            for i in r:
                if i[1]==k:
                    # rr=i[0]
                   return i[0]
            return rr
            # return r[0][0]
        except:
            return -1