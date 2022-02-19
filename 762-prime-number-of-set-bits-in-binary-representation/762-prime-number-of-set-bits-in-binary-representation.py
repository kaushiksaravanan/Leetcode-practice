d={2:1,3:1}
def prie(n):
        if n in d:
            return True
        prime_flag = 0
        if(n > 1):
            for i in range(2, int(sqrt(n)) + 1):
                if (n % i == 0):
                    prime_flag = 1
                    break
            if (prime_flag == 0):
                d[n]=1
                return True
            else:
                return False
        else:
            return False

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        c=0
        for i in range(left,right+1):
            print(i,bin(i).replace("0b",""),bin(i).count('1'),prie(bin(i).count('1')))
            if prie(bin(i).replace("0b","").count('1')):
                c+=1
        print(c)
        return c
        