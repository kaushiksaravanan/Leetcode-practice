class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        ans=0
        ke=[]
        profit=[]
        for i in range(len(profits)):
            ke.append([profits[i],capital[i]])
        ke.sort(key=lambda x:-x[0])
        # print(ke)
        # return 0
            # for j in range(i+1,len(profits)):
            #     if profits[i]<profits[j]:
            #         profits[i],profits[j]=profits[j],profits[i]
            #         capital[i],capital[j]=capital[j],capital[i]
        curr_capital=w
        while True:
            flag=0
            if k==0 or len(ke)==0:
                break
            for i in range(len(ke)):
                if k==0 or len(ke)==0:
                    flag=1
                    break
                if ke[i][1]<=curr_capital:
                    curr_capital+=ke[i][0]
                    ke.pop(i)
                    k-=1
                    break
                if len(ke)-1==i:
                    flag=1
                
            if flag==1:
                break

        # print(*profits)
        # print(*capital)
        # print(curr_capital,k)

        return curr_capital
