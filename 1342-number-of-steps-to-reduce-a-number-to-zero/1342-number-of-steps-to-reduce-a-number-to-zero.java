class Solution {
    public int no(int num,int c)
    {
        if(num==0)
            return c;
        else if(num%2==0)
            return  no(num/2,c+1);
            else
                return no(num-1,c+1);
    }
    public int numberOfSteps(int num) {
        return no(num,0);
    }
}