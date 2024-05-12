class Solution {
    public int[][] largestLocal(int[][] grid) {
        int boxSize = grid.length;
        int gridLength = boxSize - 2;

        int[][] ans = new int[gridLength][gridLength];

        for(int i = 0; i < gridLength ; i++){
            for(int j = 0; j < gridLength; j++){
                ans[i][j] = getLargest(grid, i, j);
            }    
        }

        return ans;
    }


    private int getLargest(int[][] grid, int startI, int startJ){
        int max = 0;

        for(int i = startI; i < startI + 3 ; i++){
            for(int j = startJ; j < startJ + 3; j++){
                max = Math.max(max,grid[i][j]);
            }    
        }

        return max;
    }
}