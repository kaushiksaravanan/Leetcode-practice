class Solution:
    def intToRoman(self, num: int) -> str:
        d={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',900:'CM',400:'CD',90:'XC',40:'XL',}
        s=''
        while num>0:
            for i in [1000,900,500,400,100,90,50,40,10,9,5,4,1]:
                if num>=i:
                    th=num//i
                    s+=th*d[i]
                    num=num-th*i
        return s