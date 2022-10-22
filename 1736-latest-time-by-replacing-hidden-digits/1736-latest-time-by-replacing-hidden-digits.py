class Solution:
    def maximumTime(self, time: str) -> str:
        k=''
        if time[0]=='?' and time[1]=='?':
            k+='23'
        else:
            if time[0]=='?' and int(time[1])<=3:
                k+='2'
            elif time[0]=='?' and int(time[1])>3:
                k+='1'
            else:
                k+=time[0]

            if time[1]=='?' and k[0]=='2':
                k+='3'
            elif time[1]=='?' and (k[0]=='1' or k[0]=='0'):
                k+='9'

            else:
                k+=time[1]
        k+=':'
            
        
            
        if time[3]=='?':
            k+='5'
        else:
            k+=time[3]
        if time[4]=='?':
            k+='9'
        else:
            k+=time[4]
        return k