a=[]
class MedianFinder:
    a=[]
    def __init__(self):
        a[:]=[]
        

    def addNum(self, num: int) -> None:
        a.append(num)

    def findMedian(self) -> float:
        # print(len(a),a)
        a.sort()
        if len(a)>0 and len(a)%2==0:
            return (a[len(a)//2]+a[(len(a)//2)-1])/2
        if len(a)%2!=0:
            return a[len(a)//2]
        # return 1
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()