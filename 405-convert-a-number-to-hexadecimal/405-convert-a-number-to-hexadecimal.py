class Solution:
    def toHex(self, num: int) -> str:
        he=[0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
        a=[]
        if num==0:
            return "0"
        if num<0:
            num+=2**32
        while(num>0):
            a.append(he[num%16])
            num=num//16
        if num==0:
            return "".join(str(i) for i in a[::-1])
        # if num<0:
        #     num+=2**32
        #     while(num>0):
        #         a.append(he[num%16])
        #         num=num//16
        #     return "".join(str(i) for i in a[::-1])
            
        # print()
            
        
        