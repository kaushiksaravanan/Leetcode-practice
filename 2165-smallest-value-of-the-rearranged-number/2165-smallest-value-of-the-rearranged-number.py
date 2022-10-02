class Solution:
    def smallestNumber(self, num: int) -> int:
        if num>0:
            k=[int(i) for i in str(num)]
            k.sort()
            ans=''
            if k[0]==0:
                m=k.count(0)
                print(m)
                for i in range(m):
                    k.remove(0)
                # ar=[k[:i]]+['0']*m+k[i:]
                # if len(k)>=1:
                print(k,k[2:])
                ar=[k[0]]+[0]*m+k[1:]
                return int(''.join([str(i) for i in ar]))
            else:
                return int("".join([str(i) for i in k]))
        elif num==0:
            return 0
        else:
            k=[int(i) for i in str(num)[1:]]
            k.sort()
            k=k[::-1]
            ans=''
            # if k[-1]==0:
                # ar=[k[1]]+[k[0]]+k[:-1]+[k
                # return int(''.join([str(i) for i in ar]))
            # else:
            return -int("".join([str(i) for i in k]))
                
            