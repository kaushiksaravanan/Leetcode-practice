class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, ma: int) -> bool:
        pos=[(-1,-1),(-1,0),(1,0),(0,1),(1,1),(-1,1),(1,-1),(0,-1),(0,0)]
        distance=max(abs(sx-fx),abs(fy-sy))
        if distance==0:
            return True if ma>1 or ma==0 else False
        if distance>ma:
            return False
        return True
        # pos.sort()
        print(pos)
        @cache
        def rec(i,j,t):
            print(i,j,t)
            if t>ma:
                return False
            if i==fx and j==fy:
                if t==ma:
                    return True
                else:
                    return False
            else:
                for ir in pos:
                    print(ir[0]+i,ir[1]+i,t+1)
                    k=rec(ir[0]+i,ir[1]+i,t+1)
                    if k:
                        return True
                return False
        return rec(sx,sy,0)

        