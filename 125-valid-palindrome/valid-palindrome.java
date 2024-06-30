class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        
        String p = "";
        
        for (int i = 0; i < s.length(); i ++){
            char c = s.charAt(i);
            
            if((c >= 'a' && c <= 'z') || (c >= '0' && c <='9')){
                p += c;
            }
            
            
        }
                
        int i = 0;
        int j = p.length() - 1;
                
        while(i < j){
            if(p.charAt(i) != p.charAt(j))
            {
                return false;
            }
            
            i++;
            j--;
        }
        
        return true;
        
        
    }
}