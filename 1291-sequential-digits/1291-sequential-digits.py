class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        xe=[]
        y=[1,2,3,4,5,6,7,8,9]
        for _ in range(len(str(low)),len(str(high))+1):
            for i in range(9-_+1):
                r=int("".join((str(i) for i in y[i:_+i])))
                if r>=low and r<=high:
                    xe.append(r)

                
            # print('x and y',x,y,end=' ')
            # if x==y and x!=0 and y!=0:
            #     xe.append(i)
            #     # if prev==int(str(i)[-1]):
            #     if int(str(i)[-1])==prev:
            #         k.append(i)
        print(xe)
        return xe
                
                    
                