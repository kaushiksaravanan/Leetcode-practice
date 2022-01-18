

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n){
    int i=0,k=0;
    
    
        while(i<flowerbedSize){
                if( flowerbed[i]==0 && (i==0 || flowerbed[i-1]==0) &&(i==flowerbedSize-1 || flowerbed[i+1]==0))
                {flowerbed[i]=1;
                    k+=1;}
            i+=1;
        }
    return k>=n;
}