class Solution {
    public String simplifyPath(String path) {
        Deque<String> s = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();
        
        for(char c : path.toCharArray()){
            
            if(c == '/'){
                if(sb.length() == 0){
                    continue;
                }
                
                String t = sb.toString();
                sb.setLength(0);
                
                if(t.replace(".", "").length() == 0 ){
                    int l = t.length();
                    
                    if(l > 2){
                        s.offerLast(t);
                    } else if(l == 2){
                        s.pollLast();
                    }
                    
                } else {
                    s.offerLast(t);
                }
                
            } else{
              sb.append(c);
            }
            
        }
        
        if(sb.length() > 0){
            String t = sb.toString();
            sb.setLength(0);

            if(t.replace(".", "").length() == 0 ){
                int l = t.length();

                if(l > 2){
                    s.offerLast(t);
                } else if(l == 2){
                    s.pollLast();
                }
            } else {
                s.offerLast(t);
            } 
        }
        
        System.out.println(s);
        
        
        while(!s.isEmpty()){
            sb.append('/').append(s.pollFirst());
        }
        
        if(sb.length() == 0){
            return "/";
        } else {
            return sb.toString();
        }
        
    }
}