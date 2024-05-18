class Solution {
    public int mySqrt(int x) {
        int l = 0;
        int r = x;
        int mid = -1;
        long a = -1;
        
        while(l <= r){
            mid = l + (r-l) /2;

            if((long) mid * mid > (long) x){
                r = mid -1;
            } else if( mid * mid == x){
                return mid;
            } else {
                l = mid + 1;
            }
            
        }        
        
        return r;
    }
}