class Solution {
    public int alternateDigitSum(int n) {
        ArrayList<Integer> d=new ArrayList<Integer>();
        d.add(1);
        while(n>0)
        {
            d.add(n%10);
            n=n/10;
        }
        int s=0;
        int k=1;
        for(int i=d.size()-1;i>0;i--)
        {
            s=s+k*d.get(i);
            System.out.println(d.get(i));
            k=k*-1;
        }
        return s;
    }
}