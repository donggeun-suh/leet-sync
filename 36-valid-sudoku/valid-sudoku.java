class Solution {
    public boolean isValidSudoku(char[][] board) {
        int[] visited = new int[10];
        char c = '*';
        
        for(int i = 0; i < 9; i ++){
            for(int j = 0; j < 9; j ++){
                
                c = board[j][i];
                
                if(Character.isDigit(c)){
                    if(visited[c - '0'] == 1){
                        return false;
                    }
                    visited[c - '0'] = 1; 
                }
                
            }
            
            visited = new int[10];
        }
        
        for(int i = 0; i < 9; i ++){
            for(int j = 0; j < 9; j ++){
                c = board[i][j];
                
                if(Character.isDigit(c)){
                    if(visited[c - '0'] == 1){
                        return false;
                    }
                    visited[c - '0'] = 1; 
                }
            }
            
            visited = new int[10];
        }
        
        for(int i = 0; i < 9; i += 3){
            for(int j = 0; j < 9; j += 3){
                
                for(int p = i; p < i + 3; p ++){
                    for(int q = j; q < j + 3; q ++){
                        c = board[p][q];
                
                        if(Character.isDigit(c)){
                            if(visited[c - '0'] == 1){
                                return false;
                            }
                            visited[c - '0'] = 1; 
                        }
                    }
                }
                
                visited = new int[10];

            }
        }
        
        return true;
        
    }
}