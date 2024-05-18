class Solution {
    public int mySqrt(int x) {
        int k = 0;
        
        while(true){
            long a = (long) k * k;
            if(a > x){
                break;
            }
            
            k = k + 1;
        }
        
        return k -1;
        
    }
}