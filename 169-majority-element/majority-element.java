class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> countMap = new HashMap<>();
        Integer count = null;
        int majority = 1 +  nums.length / 2; 
        
        for(int i  = 0; i < nums.length; i++) {
           count = countMap.getOrDefault(nums[i], 0);
            

            countMap.put(nums[i], count + 1);
            
            if (count + 1 >= majority){
                    return nums[i];
            }
        }
        
        return -1;
    }
}

