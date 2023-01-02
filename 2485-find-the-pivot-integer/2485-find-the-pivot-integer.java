class Solution {
    public int pivotInteger(int n) {
        int sum_till_pivot=0;   
        int sum_after_pivot=0;
        if(n<=1)
            return n;
        for(int pivot=0;pivot<n;pivot++)
        {
            sum_till_pivot=(pivot)*(pivot+1)/2;
        sum_after_pivot=pivot*(n-pivot+1)+(((n-pivot)*(n-pivot+1))/2);
            System.out.println(sum_till_pivot+" "+sum_after_pivot);
            if(sum_till_pivot==sum_after_pivot)
                return pivot;
        }
        return -1;
        
    }
}