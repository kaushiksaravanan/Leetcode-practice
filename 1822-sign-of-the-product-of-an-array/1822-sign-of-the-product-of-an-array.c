

int arraySign(int* nums, int numsSize){
    int l=0;
    for(int i=0;i<numsSize;i++)
    {if(nums[i]<0)
            l+=1;
        if(nums[i]==0)
            return 0;}
    if(l%2!=0)
        return -1;
    else
        return 1;
}