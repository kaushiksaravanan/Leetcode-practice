class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        a=[]
        for i in grid:
            a.append(i)
        aa=[]
        for i in range(len(grid[0])):
            k=[]
            for j in range(len(grid)):
                k.append(grid[j][i])
                print(grid[j][i])
                # print(j,i)
            print()            
            aa.append(k)
        print(a)
        print(aa)
        c=0
        for i in a:
            if i in aa:
                c+=aa.count(i)
        return c