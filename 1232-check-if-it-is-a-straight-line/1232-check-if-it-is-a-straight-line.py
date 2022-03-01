class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)<=2:
            return True
        prev_a=(coordinates[1][1]-coordinates[0][1])
        prev_b=(coordinates[1][0]-coordinates[0][0])
        if prev_b==0:
            prev='inf'
        else:
            prev=prev_a//prev_b
        print(prev)
        for i in range(1,len(coordinates)-1):
            a=(coordinates[i+1][1]-coordinates[i][1])
            b=(coordinates[i+1][0]-coordinates[i][0])
            if b==0:
                k='inf'
            else:
                k=a//b
            print(k,prev,k==prev)
            if prev!=k:
                return False
            prev=k
            prev_a=a
            prev_b=b
        return True
                        