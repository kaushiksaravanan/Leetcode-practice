class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        ans=0
        ke=[]
        profit=[]
        for i in range(len(profits)):
            ke.append([profits[i],capital[i]])
        ke.sort(key=lambda x:-x[0])
        # curr_capital=w
        n=len(ke)
        while True:
            flag=0
            if k==0 or len(ke)==0:
                break
            for i in range(n):
                if k==0:
                    flag=1
                    break
                if ke[i][1]<=w:
                    w+=ke[i][0]
                    ke.pop(i)
                    k-=1
                    n-=1
                    break
                if n-1==i:
                    flag=1
            if flag==1:
                break
        return w